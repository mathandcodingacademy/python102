# Week 3 — Lists and Dictionaries

Until now, every variable has held one thing — one number, one string, one name. This week you learn two data structures that hold many things at once: **lists** (ordered collections) and **dictionaries** (lookup by name instead of position).

By the end of this week, you'll store real collections of data properly instead of typing values in one at a time — the same way grades, inventories, and contact lists are stored in actual software.

## Files in this folder

| File | What it covers |
|---|---|
| `01_lists_and_dicts.py` | Lists, iterating over lists, dictionaries, iterating over dictionaries, and lists of dictionaries |
| `02_exercises.py` | Tasks to do on your own — grocery list, contact book, grade book, bonus word frequency |
| `03_mini_project.py` | A complete menu-driven app — Class Grade Tracker — that puts everything together in one real program |

## Read these in order

`01_lists_and_dicts.py` has 5 programs, each building on the last. Run each one before moving to the next, and try the `CHALLENGE` at the end of each program — they set up ideas you'll need in `02_exercises.py` and `03_mini_project.py`.

`03_mini_project.py` is the payoff for the week: a menu loop (already built for you) that's missing 5 functions. Fill them in and you have a working app, not just a script.

## What you need before starting

- Comfortable with: variables, functions, `for` loops, `if`/`elif`/`else` (Python101 + Weeks 1–2)
- Your Week 2 GitHub repo, ready to `add`, `commit`, and `push` your work this week too

## The two structures, in one line each

> **List** — `["Amelia", "Noah", "Priya"]` — ordered, found by index (`names[0]`).
> **Dictionary** — `{"name": "Amelia", "grade": 88}` — unordered, found by key (`student["name"]`).

If you need to ask "what's the 3rd thing?" — use a list.
If you need to ask "what's this thing's grade?" — use a dictionary.

## Looking ahead

Next week (File I/O and Data Persistence) you'll learn to save a list of dictionaries — like `class_records` from `01_lists_and_dicts.py`, or the `roster` you build in `03_mini_project.py` — to a file, so your data doesn't disappear every time you close VS Code. Everything you build this week is what gets saved next week.
