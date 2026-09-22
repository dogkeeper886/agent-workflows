---
description: >-
  An agent writes a README by its own ideas. The agent copies the existing
  docs and its memory of README convention. The copied claims are stale
  before the README ships. The key points a newcomer needs go undrawn, and a
  diagram exported by hand cannot be rendered again. This skill asks the agent
  to write a README by the steps below, not by its own ideas.
---

Write a README:
1. Search the web for this year's README convention, and note the sources.
2. Study the project from its code, build files and config, and read its existing docs only as claims to check.
3. Number the key points a newcomer needs, the idea that makes the parts one whole first.
4. Draw one SVG per key point in `docs/diagrams/`, with no Mermaid.
5. Render each SVG to PNG with a command committed in the project, `rsvg-convert -z 2 <name>.svg -o png/<name>.png` by default.
6. Open the README with one paragraph: {situation}. {complication}. {question}. {answer}.
7. Follow it with the key points, each with its PNG.
8. Check every command, path, env var and link in the README against the code.
9. Gate the README with the `review-readme` skill.
