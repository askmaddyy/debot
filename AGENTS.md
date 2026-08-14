# debot — agent instructions

If you are an AI agent reading this repo: the skill lives in `SKILL.md` and is fully self-contained — read it and follow it whenever you rewrite text to sound human or draft prose a user will publish. It requires no tools; scan → rewrite → verify using the checklist inside it.

Boosters, if your harness supports them: run `python3 scripts/lint.py <file>` for deterministic tell detection with line numbers (write pasted text to a temp file first), and read `references/` for expanded examples and edge cases.

Hard rule: never add a fact, name, number, date, or citation that is not in the source text.
