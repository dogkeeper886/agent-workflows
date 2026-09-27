---
description: >-
  An agent writes the comments in a config file by its own ideas. The agent
  describes each line in a comment. The comments drift from their lines with
  every edit. The drifted comments confuse the reader, and the confused reader
  edits in the wrong direction. A value lives in a config file only because it
  can change, so the reader needs each option and its range, not a description
  of the line. This skill asks the agent to review a config file's comments by
  the steps below, not by its own ideas.
---

Config comment review:
1. Create a Markdown file in the scratchpad.
2. The Markdown file holds a header and a list.
3. The header holds the config file path.
4. The list holds the config file comments.
5. Strike through each comment that describes its line.
6. Strike through each comment that holds a note, a reason or a history.
7. Add each value a reader can change to the list.
8. Put each value's options or range after it, read from the program that takes the value.
9. Rewrite the config file comments as one comment per changeable value, holding its options or range.
