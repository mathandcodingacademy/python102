# 03 – The Python Extension for VS Code

## What is an extension?

VS Code on its own is just a text editor — it doesn't know Python from a plain text file.

Extensions add intelligence to VS Code. The Python extension teaches VS Code about Python specifically: it knows the syntax, the built-in functions, and how to run your code.

---

## Install the Python Extension

1. Click the **Extensions icon** in the left sidebar (puzzle piece icon, or `Ctrl + Shift + X`)
2. In the search bar, type: `Python`
3. The first result should be **Python** by **Microsoft** (look for the verified checkmark and tens of millions of installs)
4. Click **Install**

---

## What it gives you

### Syntax highlighting
Your code is colour-coded. Keywords like `if`, `for`, `def` are one colour. Strings are another. Numbers another. This makes code much easier to read and spot mistakes in.

### IntelliSense (autocomplete)
Start typing `prin` — VS Code will suggest `print`. Press Tab to complete it.
Type `print(` and pause — VS Code shows you what arguments the function accepts.

Try it in `practice.py` from the last file.

### Inline error detection
VS Code underlines problems in your code **before you even run it**. A red underline means a syntax error. A yellow underline is a warning.

Try typing this deliberately broken code:

```python
x = 10
if x > 5
    print("big")
```

You'll see a red underline on the `if` line — missing colon. Fix it to `if x > 5:` and the underline disappears.

### Python version selector
Look at the **bottom status bar** — you should now see a Python version (e.g. `3.12.1`).
Click it to see all Python versions installed on your machine and choose which one VS Code uses.

---

## ✅ Checklist

- [ ] Python extension by Microsoft is installed
- [ ] You can see the Python version in the bottom status bar
- [ ] IntelliSense autocomplete works — you saw a suggestion pop up
- [ ] You triggered a syntax error and saw the red underline

Once all done, open `04_programs.py`.
