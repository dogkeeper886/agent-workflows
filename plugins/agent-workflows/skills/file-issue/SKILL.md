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
3. Ensure the created issue holds only one section, the step 2 result.
4. Ensure the repo's `.gitignore` holds `.sessions/`.
5. Copy the session log, `~/.claude/projects/*/$CLAUDE_CODE_SESSION_ID.jsonl`, to the repo's `.sessions/`.
6. Mask each value in the copy that grants access or identifies a person, a device or a private network.
7. Name the copy's path in an issue comment.
8. When an action on the log is blocked and the task can finish in the current session, skip the log.
9. When an action on the log is blocked and the task needs to cross sessions, tell the user.
