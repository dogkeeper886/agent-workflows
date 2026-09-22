---
description: >-
  An agent reviews the words of a document by its own ideas. The agent
  applies one register to every file. A markdown file declares no contract,
  and the same wording is right in a talk track and wrong in a test case. The
  agent cannot hear its own register, so it passes its own tells. This skill
  asks the agent to review the words of a document by the steps below, not by
  its own ideas.
---

Review the words of a document:
1. Name the document's kind, its reader and the action it enables, and ask when the file does not say.
2. Read the matching file in `reference/` when the kind has one.
3. Run `"$CLAUDE_PLUGIN_ROOT"/skills/reviewing-phrasing/check-prose.sh <file>`, or the `check-prose.sh` beside this file outside a plugin.
4. Count a hit as a finding only when it costs this reader.
5. Read for what the script cannot catch: the "isn't A, it's B" frame, triads, restatement, vague claims and uniform sentence length.
6. Judge purpose first, then structure, then accuracy, then sentences.
7. Report with the `reporting-outcomes` skill, quoting the words at fault and saying which findings came from the script.
