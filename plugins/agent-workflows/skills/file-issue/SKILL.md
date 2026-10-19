---
description: >-
  An agent files an issue by its own ideas. The agent rewrites each request
  in its own words. The rewritten request shifts the intent before anyone
  notices. The shifted issue drops the reasoning behind it. A cold agent
  picks the issue up and builds the shifted intent. The session log that
  carries the reasoning can also carry a secret into a public repository. This
  skill asks the agent to file an issue by the steps below.
---

File an issue:
1. Open the issue with an SCQA opening structure: {context the reader already agrees with}. {the change that disrupts it}. {the issue it raises, stated or as its consequence}. {what resolves it}.
2. Rewrite the step 1 result with the `rewrite-phrasing` skill.
3. Link the session log to the issue, uploaded to an issue comment or the repo's .sessions/ when possible. When an action on the log is blocked, skip the log if the task can finish in the current session, and tell the user if the task needs to cross sessions.
4. Ensure the created issue holds only one section, the step 2 result.