---
description: >-
  An agent reviews a skill, command, rule or CLAUDE.md by its own ideas. The
  agent reads the file and finds each line fine on its own. A stale reference,
  a rule restated four times and a unit that duplicates another all read fine
  on their own. The file keeps its place and drifts. This skill asks the agent
  to review an artifact an agent reads by the steps below, not by its own
  ideas.
---

Review an artifact:
1. Say in one sentence what the artifact is for, and flag each part that does not serve it.
2. Find any other artifact that does the same job.
3. Check the description says what the unit does and when to reach for it.
4. Flag an `allowed-tools` key, with deleting it as the fix.
5. Resolve every path, filename, command and cross-reference by grep, not by reading.
6. Flag a path, label or tool frozen where the project owns the choice.
7. Flag a rule stated more than once, and emphasis on a step nobody has seen dropped.
8. Flag anything the body does that its description does not imply.
9. Report with the `reporting-outcomes` skill; for a duplicate, recommend cutting it and name what absorbs the job.
10. Merge, split or delete an artifact only on the user's yes.
