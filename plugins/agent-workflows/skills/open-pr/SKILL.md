---
description: >-
  An agent opens a pull request by its own ideas. The agent that wrote the
  work grades it done. The self-graded work hides the gap between what was
  asked and what was built. The hidden gap reaches the person who reviews the
  pull request. This skill asks the agent to open a pull request by the steps
  below, not by its own ideas.
---

Open a pull request:
1. Read the issue and the session log it links, before the diff.
2. Review the diff against what the issue asked, and find what the change left behind.
3. When the review fails, stop and report with the `reporting-outcomes` skill.
4. Write the pull request as an SCQA intro, then the answer as a list of topic: comment.
5. Open the pull request.
6. Print the pull request's intro in the session.
