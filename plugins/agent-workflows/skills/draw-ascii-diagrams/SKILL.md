---
description: >-
  An agent answers a question about a sequence, a dependency or a flow. The
  agent writes each part as a sentence, in the order it thought of them. A
  sentence carries one path at a time, so a branch, a loop and a blocked step
  all read as another sentence. The reader rebuilds the shape in their head.
  This skill asks the agent to redraw its previous response as ASCII diagrams
  by the steps below.
---

Draw the previous response:
1. Report the previous response with the `reporting-outcomes` skill.
2. Save the report to a temp file.
3. Under each header, list each clause's main character in bold and its action in a code span.
4. Pick each header's diagram kind from its list.
5. Draw that diagram in ASCII under the list, characters as boxes and actions as arrows.
6. Check each diagram against its list.
7. Replace each header's text and list with its diagram.
8. Render the report to the session.
