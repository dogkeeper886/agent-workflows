---
description: >-
  An agent fixes a text's phrasing by its own ideas. The agent hands back only
  the rewrite. The rewrite hides which subject, action, filler, negative or
  hidden action it changed. The reader can neither check the rewrite nor learn
  from it. This skill asks the agent to study a text's phrasing by the steps
  below.
---

Review sentences:
1. On the input text, bold each sentence's subject and put its action in a code span.
2. On the step 1 result, strike through redundancy and bloat.
3. Output the step 2 result with its marks and strike-throughs in a quote block under "Bloat struck", then a clean version with the struck words removed and no marks under "Clean".
4. On the step 3 clean output, bold the character that should be central and put its action in a code span, when it has one.
5. On the step 4 result, strike through each sentence with its central character outside the subject and put its rewrite after it, with the character as the subject and its action as the verb.
6. Output the step 5 result with its marks and strike-throughs in a quote block under "Central characters", then a clean version with the struck sentences removed and no marks under "Subjects".
7. On the step 6 clean output, strike through each negative sentence and put its affirmative rewrite after it.
8. Output the step 7 result with its marks and strike-throughs in a quote block under "Negatives rewritten", then a clean version with the struck sentences removed and no marks under "Affirmative".
9. On the step 8 clean output, strike through each sentence with a nominalization that hides an action and put its verb rewrite after it.
10. Output the step 9 result with its marks and strike-throughs in a quote block under "Nominalizations", then a clean version with the struck sentences removed and no marks under "Verbs".
