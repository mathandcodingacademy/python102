# Python102 – AI-Powered Python Projects

**Math+Coding Academy** | mathcoding.ca

This is the course repository for Python102. Students build three real AI-powered projects
over the term, using AI tools in VS Code (mostly GitHub Copilot, some use other AI
assistants) to write code — and developing the skills to read, verify, and fix what
the AI produces.

---

## Prerequisites

Completion of Python101: variables, input/output, conditionals, loops, functions,
lists, dictionaries, file I/O, basic debugging.

Python 3.10+, VS Code, and Git should already be installed from Python101.

---

## Course Outline

| Week(s) | Folder | Topic | Format |
|---------|--------|-------|--------|
| 1 | `week1/` | Python recap + OOP intro: classes, objects, `__init__`, `self` | 30 min deck + 30 min practice |
| 2 | `week2/` | OOP in practice: methods, objects working together, `__str__`, class attributes, a class that holds a list | 4 short lesson + your-turn pairs |
| 3 | `week3/` | Error handling: `try/except`, `raise`, your own error type | 4 short lesson + your-turn pairs |
| 4 | `week4/` | Modules: `math`, `random`, `datetime`, `json`, `os` | 4 short lesson + your-turn pairs |
| 5 | `week5/` | Mini project (no AI): High Score Tracker | 5 short pairs, then run `05_app.py` |
| 6 | `week6/` | Introduction to AI + using AI tools in VS Code | 30 min deck + 30 min hands-on |
| 7–8 | `week7-8/` | **Project: AI Weather Mood App** — live weather API + Tkinter GUI | Project guide + reference files |
| 9–10 | `week9-10/` | **Project: AI Trash Sorter** — train your own model + webcam classifier | Project guide + reference file |
| 11 | `week11/` | Debugging AI code — finding silent bugs, intro to `unittest` | Concept + lesson + exercise |
| 12 | `week12/` | **Final Project Showcase** — build something of your own choosing with AI | Project guide |

---

## How to Use This Repo

Different weeks use different file formats depending on what that week needs:

| File | Where you'll find it | What it's for |
|------|---------------------|---------------|
| `deck.md` | `week1/`, `week6/` | Gamma-friendly slide deck for the theory portion of class. Paste into [gamma.app](https://gamma.app) to auto-generate slides. |
| `README.md` | Every week | Concept explanation, instructions, and checkpoints for that week |
| `01_lesson.py`, `01_your_turn.py`, ... | `week2/` through `week5/` | Short activities in order. Start at that week's `README.md`. Done when the file prints `PASSED`. |
| `05_app.py` | `week5/` | The finished High Score Tracker. Run it after the week's activities pass. |
| `hands_on.py` | `week6/` | In-class AI tool activities |
| `weather.py`, `app.py` | `week7-8/` | Reference implementations — build your own with AI first |
| `sorter.py` | `week9-10/` | Reference implementation — build your own with AI first |

---

## The Project Weeks (7–8, 9–10, 11–12)

These weeks follow an **incremental AI build** approach:
- You build the project in 4 small steps, not one big prompt
- Each step has a short, specific prompt to give the AI
- Each step has a **"Common AI mistake"** section telling you what the AI typically gets wrong there — and how to catch and fix it
- You verify each step works before moving to the next

The goal is not just a working app — it's developing the habit of **reading, testing, and owning** every line of AI-generated code.

---

## Setup

```bash
# Clone this repo (if you haven't already)
git clone https://github.com/mathandcodingacademy/python102.git
cd python102
code .
```

Install dependencies as needed each week — each project's `README.md` lists what's required.
