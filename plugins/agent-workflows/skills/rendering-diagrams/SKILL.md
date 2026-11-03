---
description: >-
  An agent writes a document's processes, structures and relationships as
  sentences. A section past 111 words outgrows its reader: users read about
  half of a page only when it holds 111 words or less (Nielsen, 2008). The
  reader skims the section and rebuilds its order, branches and links in their
  head. This skill asks the agent to draw each such section as a diagram by
  the steps below.
---

Draw a document's diagrams:
1. Find each section that runs past 111 words, counting its subsections, and describes a process, a structure or relationships.
2. List each section's characters in bold and their actions in code spans in a scratchpad file.
3. Pick each section's diagram kind from its step 2 list.
4. Draw each diagram as an SVG in `docs/diagrams/`, characters as boxes and actions as labeled arrows.
5. Render each SVG to PNG in `docs/diagrams/` with `rsvg-convert -z 2 <name>.svg -o png/<name>.png`.
6. Read each PNG, and check every box, arrow and label against its step 2 list and for overlap.
7. Repeat steps 4 to 6 on each diagram that fails the check.
8. Reference each PNG under its section's first paragraph with a Markdown image link, keeping every word of the document as it is.
