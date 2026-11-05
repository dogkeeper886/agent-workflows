---
description: >-
  An agent writes a repo's test scripts from its code. A code change breaks a
  script, and the agent fixes the script to pass on the new code. The fixed
  script checks what the code does now, and drifts from the purpose the test
  was written for. A reader finds that purpose only in the script's code. This
  skill asks the agent to draw the user's session from the code as a decision
  tree, and outline its suites and case names for a person to review before any
  script exists, by the steps below.
---

# Outline a repo's test suites and case names from a decision tree of the user's session

1. Read the repo's code, taking a claim from its docs only where the code confirms it.
2. Copy this skill's `decision-tree-template.md` to `test-cases/decision-tree.md`, leaving the repo's own files as they are.
3. Write a tree under its own heading for each person the code serves, starting at that person's first action.
4. Write each step of that person's session as a stage, in the order a session meets them.
5. Write each choice a stage meets as a decision under it, with one answer under it per branch the code takes on that choice.
6. Mark each decision `user` when the person makes it or meets it while using the product, `setup` when it readies the product or its host before that use, or `build` when it builds, releases or debugs the product.
7. Hang under each answer of a `user` decision a case name for the answer and for each boundary and error the code checks on it that the person can cause from outside the code, by `[Action] [object] with [the condition that sets this case apart][ and the shared condition]`, or `[Action] [object] with [the shared condition]` when the action sets the case apart.
8. Run `python3 <this skill's folder>/draw_decision_tree.py test-cases/decision-tree.md` to check the tree, draw its SVG and PNG, and write `test-cases/suites.md`.
9. Fix what the script names when it refuses the tree, then run it again.
