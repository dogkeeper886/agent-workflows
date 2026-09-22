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
4. Write the pull request's intro as an SCQA opening structure: {context the reader already agrees with}. {the change that disrupts it}. {the issue it raises, stated or as its consequence}. {what resolves it}.
5. Follow the intro with the answer's details as a list of topic: comment.
6. Commit the work and push the branch.
7. Open the pull request.
8. Print the pull request's intro in the session.
