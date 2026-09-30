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
1. Study the previous response with the `article-structure-study` skill.
2. Report it with the `reporting-outcomes` skill.
3. Save the report to a temp file.
4. Rewrite the study with the `reviewing-phrasing` skill, taking each section's main character from the report's header.
5. Pick each header's diagram kind from its text.
6. Replace each header's text with that diagram in ASCII.
7. Check each diagram against the study.
8. Render the report to the session.
