"""Check a decision tree, draw it as an SVG and a PNG, and write its suites.

usage: draw_decision_tree.py <decision-tree.md>

The tree file holds one tree under each `## <actor>` heading, the user's first:

  - [<label> → ]<stage>      a stage; <label> names the arrow into it, "then" by default
    - <decision> [<kind>]    <kind> is user, setup or build
      - <answer>             one branch of the decision
        - <case name>        a case name hung on that branch, under user decisions only

Every answer of a user decision holds at least one case name, no case name
hangs twice, and no two user decisions share a name.

Writes <decision-tree>.svg and <decision-tree>.png beside the tree file, and
suites.md there too: one suite per user decision, its case names under it.
Exits 0 when written, 1 with each problem named when the tree breaks a rule.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

KINDS = ("user", "setup", "build")
FONT = "DejaVu Sans"
CHAR_W = 7.4                      # average DejaVu Sans glyph width at 13px
STAGE_X, STAGE_W = 40, 270
DEC_X, DEC_W = 420, 190          # DEC_W is the narrowest a decision box gets
GROUP_MAX_W = 860
ROW_H, ROW_GAP, STAGE_GAP, TREE_GAP = 38, 10, 56, 70
CHIP_H, CHIP_PAD, CHIP_GAP, LINE_GAP = 26, 12, 8, 6
COLORS = {  # decision box fill, decision stroke, chip fill, chip stroke, chip text
    "user": ("#ffffff", "#3730a3", "#dbeafe", "#2563eb", "#1e3a8a"),
    "setup": ("#f1f5f9", "#64748b", "#e2e8f0", "#64748b", "#334155"),
    "build": ("#fffbeb", "#b45309", "#fef3c7", "#b45309", "#78350f"),
}


def parse(path):
    """Return the trees in the file and the problems found, as (trees, problems)."""
    trees, problems = [], []
    last_level = None
    for no, raw in enumerate(path.read_text().splitlines(), 1):
        where = f"{path.name}:{no}"
        if not raw.strip():
            continue
        if "{{" in raw:
            problems.append(f"{where}: fill the placeholder in '{raw.strip()}'")
            continue
        if raw.startswith("## "):
            trees.append({"actor": raw[3:].strip(), "stages": []})
            last_level = None
            continue
        m = re.match(r"^( *)- (.+)$", raw)
        if not m or len(m.group(1)) % 2 or len(m.group(1)) > 6:
            problems.append(f"{where}: write a list item indented by 0, 2, 4 or 6 spaces")
            continue
        if not trees:
            problems.append(f"{where}: put a '## <actor>' heading above the first stage")
            continue
        level, body = len(m.group(1)) // 2, m.group(2).strip()
        if level > (-1 if last_level is None else last_level) + 1:
            problems.append(f"{where}: '{body}' sits deeper than the item above allows")
            continue
        last_level = level
        stages = trees[-1]["stages"]
        if level == 0:
            label, _, stage = body.rpartition(" → ")
            stages.append({"label": label or "then", "name": stage, "decisions": [], "line": where})
        elif level == 1:
            d = re.match(r"^(.*\S) \[(\w+)\]$", body)
            if not d or d.group(2) not in KINDS:
                problems.append(f"{where}: end decision '{body}' with [user], [setup] or [build]")
                d_name, kind = body, "setup"
            else:
                d_name, kind = d.group(1), d.group(2)
            stages[-1]["decisions"].append({"name": d_name, "kind": kind, "answers": [], "line": where})
        elif level == 2:
            stages[-1]["decisions"][-1]["answers"].append({"name": body, "cases": []})
        else:
            stages[-1]["decisions"][-1]["answers"][-1]["cases"].append((body, where))
    for tree in trees:
        if not tree["stages"]:
            problems.append(f"{path.name}: give '## {tree['actor']}' at least one stage")
        for stage in tree["stages"]:
            if not stage["decisions"]:
                problems.append(f"{stage['line']}: give stage '{stage['name']}' at least one decision")
            for dec in stage["decisions"]:
                if not dec["answers"]:
                    problems.append(f"{dec['line']}: give decision '{dec['name']}' at least one answer")
    problems += check_cases(trees)
    return trees, problems


def user_decisions(trees):
    """Yield each user decision in reading order."""
    for tree in trees:
        for stage in tree["stages"]:
            for dec in stage["decisions"]:
                if dec["kind"] == "user":
                    yield dec


def check_cases(trees):
    """Return the problems with where the case names hang."""
    problems, hung, named = [], {}, {}
    for tree in trees:
        for stage in tree["stages"]:
            for dec in stage["decisions"]:
                for ans in dec["answers"]:
                    if dec["kind"] != "user" and ans["cases"]:
                        problems.append(f"{ans['cases'][0][1]}: drop the case names under "
                                        f"[{dec['kind']}] decision '{dec['name']}'")
                    if dec["kind"] == "user" and not ans["cases"]:
                        problems.append(f"{dec['line']}: hang a case name on answer '{ans['name']}' "
                                        f"of '{dec['name']}'")
                    for name, where in ans["cases"]:
                        if name in hung:
                            problems.append(f"{where}: '{name}' already hangs at {hung[name]}")
                        hung.setdefault(name, where)
    for dec in user_decisions(trees):
        if dec["name"] in named:
            problems.append(f"{dec['line']}: rename decision '{dec['name']}'; "
                            f"{named[dec['name']]} has the name")
        named.setdefault(dec["name"], dec["line"])
    return problems


def suites(trees):
    """Return the user decisions as a nested list of suites and case names."""
    out = []
    for dec in user_decisions(trees):
        out.append(f"- {dec['name']}")
        out += [f"  - {name}" for ans in dec["answers"] for name, _ in ans["cases"]]
    return "\n".join(out) + "\n"


def text_w(t, size=13):
    return len(t) * CHAR_W * size / 13


def draw(trees):
    """Return the trees drawn as an SVG document."""
    out = []

    def text(x, y, t, size=13, weight="normal", anchor="start", fill="#1f2937"):
        out.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
                   f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{escape(t)}</text>')

    def rect(x, y, w, h, fill, stroke, rx=6, dash=None, width=1.5):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{d}/>')

    def line(x1, y1, x2, y2, color, marker=None):
        m = f' marker-end="url(#{marker})"' if marker else ""
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                   f'stroke="{color}" stroke-width="1.6"{m}/>')

    def layout_chips(dec):
        """Return chip boxes as (x, line, w, label) and the number of lines."""
        chips, x, ln = [], 0, 0
        for ans in dec["answers"]:
            label = f"{ans['name']} ({len(ans['cases'])})" if dec["kind"] == "user" else ans["name"]
            w = text_w(label) + 2 * CHIP_PAD
            if x and x + w > GROUP_MAX_W:
                x, ln = 0, ln + 1
            chips.append((x, ln, w, label))
            x += w + CHIP_GAP
        return chips, ln + 1

    def dec_label(dec):
        total = sum(len(a["cases"]) for a in dec["answers"])
        return f"{dec['name']} ({total})" if dec["kind"] == "user" else dec["name"]

    decs = [dec for tree in trees for stage in tree["stages"] for dec in stage["decisions"]]
    dec_w = max([DEC_W] + [text_w(dec_label(d)) * 1.1 + 28 for d in decs])
    group_x = DEC_X + dec_w + 36

    y, max_x = 70, 0
    for tree in trees:
        text(STAGE_X, y, tree["actor"], size=18, weight="bold", fill="#111827")
        y += 24
        boxes = []
        for stage in tree["stages"]:
            sy = y
            for i, dec in enumerate(stage["decisions"]):
                chips, lines = layout_chips(dec)
                gh = lines * CHIP_H + (lines - 1) * LINE_GAP + 8
                rh = max(ROW_H, gh)
                cy = y + rh / 2
                dfill, dstroke, cfill, cstroke, ctext = COLORS[dec["kind"]]
                line(STAGE_X + STAGE_W, cy, DEC_X, cy, "#94a3b8")
                rect(DEC_X, cy - ROW_H / 2, dec_w, ROW_H, dfill, dstroke,
                     dash="6 4" if dec["kind"] == "build" else None)
                label = dec_label(dec)
                text(DEC_X + dec_w / 2, cy + 5, label, weight="bold", anchor="middle")
                gw = max(cx + w for cx, _, w, _ in chips) + 16
                gy = cy - gh / 2
                rect(group_x, gy, gw, gh, "#f8fafc", "#cbd5e1", rx=8)
                line(DEC_X + dec_w, cy, group_x - 2, cy, "#475569", "head")
                for cx, ln, w, label in chips:
                    x0, y0 = group_x + 8 + cx, gy + 4 + ln * (CHIP_H + LINE_GAP)
                    rect(x0, y0, w, CHIP_H, cfill, cstroke, rx=12, width=1.2)
                    text(x0 + w / 2, y0 + CHIP_H / 2 + 4.5, label, anchor="middle", fill=ctext)
                max_x = max(max_x, group_x + gw)
                y += rh + (ROW_GAP if i < len(stage["decisions"]) - 1 else 0)
            h = y - sy
            rect(STAGE_X, sy, STAGE_W, h, "#e0e7ff", "#3730a3", rx=8, width=2)
            text(STAGE_X + STAGE_W / 2, sy + h / 2 + 5, stage["name"], size=14, weight="bold",
                 anchor="middle", fill="#1e1b4b")
            boxes.append((sy, h, stage["label"]))
            y += STAGE_GAP
        for (sy, h, _), (ny, _, label) in zip(boxes, boxes[1:]):
            x = STAGE_X + STAGE_W / 2
            line(x, sy + h, x, ny - 2, "#3730a3", "trunk")
            text(x + 10, sy + h + STAGE_GAP / 2 + 4, label, size=12, fill="#3730a3")
        y += TREE_GAP - STAGE_GAP

    x = STAGE_X
    for kind in KINDS:
        dfill, dstroke = COLORS[kind][:2]
        rect(x, y, 90, 28, dfill, dstroke, dash="6 4" if kind == "build" else None)
        text(x + 45, y + 19, kind, weight="bold", anchor="middle")
        x += 104
    text(x + 10, y + 19, "(n) = case names on a user branch; setup and build branches hold none.",
         size=12, fill="#64748b")
    y += 60

    w, h = int(max(max_x, x + 420) + 40), int(y)
    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>'
        '<marker id="head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#475569"/></marker>'
        '<marker id="trunk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#3730a3"/></marker>'
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{STAGE_X}" y="36" font-family="{FONT}" font-size="20" font-weight="bold" '
        f'fill="#111827">Decision tree</text>',
    ]
    return "\n".join(head + out + ["</svg>"]) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                     usage=argparse.SUPPRESS)
    parser.add_argument("tree", type=Path)
    args = parser.parse_args()

    trees, problems = parse(args.tree)
    if not shutil.which("rsvg-convert"):
        problems.append("install rsvg-convert (librsvg2-tools) to render the PNG")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"{len(problems)} problem(s); fix them and run again", file=sys.stderr)
        return 1

    svg, png = args.tree.with_suffix(".svg"), args.tree.with_suffix(".png")
    svg.write_text(draw(trees))
    subprocess.run(["rsvg-convert", "-z", "2", str(svg), "-o", str(png)], check=True)
    out = args.tree.with_name("suites.md")
    out.write_text(suites(trees))
    print(f"wrote {svg}, {png} and {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
