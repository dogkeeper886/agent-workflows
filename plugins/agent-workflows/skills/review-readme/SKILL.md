---
description: >-
  An agent reviews a README by its own ideas. The agent checks the README's
  claims line by line against its sibling docs. The code moves on, and the
  README's story drifts from what the project now solves. The reader follows
  a README that describes an older project. This skill asks the agent to
  review a README by the steps below.
---

Review a README:
1. Study the project from its code, build files and config, and read its existing docs only as claims to check.
2. Write an SCQA opening structure for the project into a scratchpad file: {context the reader already agrees with}. {the change that disrupts it}. {the issue it raises, stated or as its consequence}. {what resolves it}.
3. Compare the whole README with the scratchpad file.
4. Stop and report with the `reporting-outcomes` skill when the drift is high.
5. Save a revise evaluation in the scratchpad file when the drift is low.
6. Review the words with the `reviewing-phrasing` skill.
7. Review the look with the `reviewing-typography` skill.
8. Report with the `reporting-outcomes` skill, including the saved evaluation.
