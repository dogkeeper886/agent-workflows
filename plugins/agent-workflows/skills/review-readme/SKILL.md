---
description: >-
  An agent reviews a README by its own ideas. The agent reads the key points
  off the README it reviews. A key point the README dropped is one the agent
  never looks for. The agent checks the claims against the sibling docs, which
  are as stale as the README. The README reaches its reader unverified. This
  skill asks the agent to review a README by the steps below, not by its own
  ideas.
---

Review a README:
1. Derive the key points from the code, not from the README, and number them.
2. Check the README opens with an intro that follows the SCQA framework: situation, complication, question, answer, without the labels.
3. Check the key points follow the intro, the first one leading.
4. Check the README covers every key point.
5. Check each key point has a committed PNG with its SVG source beside it.
6. Re-render each SVG with the project's render command, at the scale of the committed PNGs, and compare.
7. Check every command, path, env var, count and link against the code.
8. Review the words with the `reviewing-phrasing` skill and the look with the `reviewing-typography` skill.
9. Report with the `reporting-outcomes` skill, each finding with its file:line and smallest fix.
