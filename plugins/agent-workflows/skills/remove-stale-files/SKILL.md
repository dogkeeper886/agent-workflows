---
description: >-
  An agent cleans up after this plugin by its own ideas. The agent deletes
  what looks old. A fork that shadows a placed skill looks current and stays.
  A file the project wrote looks old and goes. A stale file answers the next
  agent plausibly and wrongly. This skill asks the agent to remove stale files
  by the steps below, not by its own ideas.
---

Remove stale files:
1. Look for the files listed in `fork-migration.md` and `stale-documents.md` beside this file.
2. Read `~/.claude/plugins/known_marketplaces.json` before calling a fork redundant.
3. Leave every file you cannot trace to this plugin.
4. Show the user every file, what replaces it, and what goes with nothing to replace it.
5. Ask once for the whole list, and delete only on a yes.
6. In `project-profile.md`, delete only this plugin's sections.
7. Report with the `reporting-outcomes` skill, naming what was removed and what was kept.
