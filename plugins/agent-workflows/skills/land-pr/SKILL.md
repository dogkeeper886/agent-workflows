---
description: >-
  An agent merges a pull request by its own ideas. The agent reads "merge it"
  as the approval. The assumed approval lets commits land that no person
  reviewed or tested. A head that moved after the review lands with them. This
  skill asks the agent to merge a pull request by the steps below, not by its
  own ideas.
---

Merge a pull request:
1. Ask the user outright whether they reviewed and tested the pull request at its head commit, and merge only on a yes.
2. Merge pinned to the confirmed commit.
3. Confirm the merge on the remote default branch.
4. When the merge did not close the issue, close it.
5. Delete the branch on the remote and in the local copy.
6. Report the outcome with the `reporting-outcomes` skill.
