# Harness — Manual Test Checklist

No API key needed. This is a set of trick questions with checklists, meant
to catch the specific ways this skill could fail: fabricating a number,
skipping a source, or answering confidently instead of asking when it
should. Use it any time you edit SKILL.md, or every so often to spot-check.

## How to use it

1. Open `eval_cases.md`.
2. Pick a test case, paste its **Prompt** into a chat where this skill is
   loaded.
3. Read Claude's answer against that case's **Checklist**.
4. If anything fails, don't just note it and move on — open
   `memory/mistakes-log.md` and log it there in the format described in
   that file. That turns a one-off failure into a permanent lesson the
   skill checks against next time.
5. Re-run the same case later to confirm the fix stuck.

## Adding your own cases

Copy the format of an existing case at the bottom of `eval_cases.md`.
The best new cases come directly from real mistakes you catch in normal
use — anything you had to correct Claude on is worth turning into a
permanent test case here.
