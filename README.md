# agent-workflows

An agent carries a request from a Claude Code session to a merged pull request.
The agent works by its own ideas: it rewrites the request in its own words, grades its
own work done and reads *"merge it"* as approval. The merged work drifts from the
request, and its reasoning stays behind in the session log. This plugin carries the
request by four skills, `file-issue`, `do-task`, `open-pr` and `land-pr`, each a short
list of steps that stops for a person.

## The four skills

The plugin carries the reasoning from one session to the next in the session log, which
keeps how the agent read the request and thought it through. `file-issue` links the log
to the issue. `do-task` reads it and starts with the whole reasoning, so you skip
explaining, correcting and guiding it again. `open-pr` checks the work against your
request in the log. `land-pr` merges only the commit you confirmed and deletes the
branch, so the history stays clean.

### file-issue

`file-issue` turns a request into an issue with an SCQA intro. It copies the session log
into `.sessions/` and links it from the intro, so the next agent reads the reasoning behind
the request. It asks you first when the log holds a secret or private detail.

    /agent-workflows:file-issue the parser drops trailing commas

### do-task

`do-task` reads the issue, its comments and its session log whole, then does the work and
reports the outcome.

    /agent-workflows:do-task 42

### open-pr

`open-pr` reviews the work against what the issue asked. A failed review stops it with a
report; a passed review commits, pushes and opens the pull request with an SCQA intro.

    /agent-workflows:open-pr

### land-pr

`land-pr` asks whether you reviewed and tested the pull request at its head commit, and
merges that commit only on your yes. It then confirms the merge, closes the issue and
deletes the branch.

    /agent-workflows:land-pr 43

## Install

The plugin installs from this repository, which is its own marketplace:

    /plugin marketplace add dogkeeper886/agent-workflows
    /plugin install agent-workflows@agent-workflows

The plugin needs `gh` or `glab`, installed and authenticated, for every step that
touches an issue or a pull request.

## More skills

### Against drift

The agent works by its own ideas, especially when it writes. Its report buries the
verdict until it is worthless. Its comments drift from their lines until the next reader
edits the logic wrongly. A skill written to hold the agent to a task drifts too, because
the agent writes it by its own ideas, and the drift grows with every edit. These skills
hold a report, a comment and a skill to a short list of steps a person can review.

- `reporting-outcomes` opens every report with the verdict and ends it with one next
  step, so you know what to do from the first line.
- `reviewing-script-comments` rewrites a config file's comments as each value's options
  or range, so you change a value without reading the program behind it.
- `skill-structure` keeps a skill to one description and a list of steps, so you review
  it in one read.

### Article writing

- `reviewing-phrasing` puts each sentence's main character first, so you read a document
  once.
- `reviewing-typography` makes a document's point stand out and stand alone, so you find
  it at a glance.
- `article-structure-study` lists an article's sections with each clause's main
  character and action, so you see its structure in one page.

### Other

- `gen-readme` writes a README from the code with an SCQA opening, so a newcomer gets the
  point from the first paragraph.
- `review-readme` checks a README against the code, so the README you ship matches what
  it describes.
- `remove-stale-files` deletes what earlier versions of this plugin left behind, so an
  old file stops answering the next agent.
