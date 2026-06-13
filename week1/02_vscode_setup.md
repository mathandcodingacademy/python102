# 02 – Setting Up VS Code

## What is VS Code?

VS Code (Visual Studio Code) is a **code editor** made by Microsoft. It's free, runs on your computer, and is one of the most popular tools used by professional developers worldwide.

It's not a website. It's not a simplified kids' tool. Real developers use this.

---

## Step 1 – Install VS Code

1. Go to https://code.visualstudio.com/
2. Click **Download for Windows**
3. Run the installer — accept all defaults
4. On the "Select Additional Tasks" screen, check:
   - ✅ Add "Open with Code" action to Windows Explorer file context menu
   - ✅ Add to PATH

---

## Step 2 – Open VS Code and set up your workspace

A **workspace** in VS Code is just a folder you've opened. All your files, the terminal, and settings are scoped to that folder.

1. Create a folder on your Desktop called `python102`
2. Open VS Code
3. Go to **File → Open Folder** → select your `python102` folder
4. You'll see the folder appear in the **Explorer panel** on the left

---

## Step 3 – Learn the VS Code layout

Take 5 minutes to find each of these — you'll use them every class:

| Area | Where it is | What it does |
|---|---|---|
| Explorer | Left sidebar (file icon) | Shows your files and folders |
| Editor | Centre | Where you write code |
| Terminal | Bottom panel | Where you run code |
| Extensions | Left sidebar (puzzle piece icon) | Where you install tools |
| Status Bar | Very bottom strip | Shows Python version, git branch, errors |

**Open the terminal:**
Go to **View → Terminal** or press `Ctrl + \``

You should see a terminal at the bottom of VS Code. Type:
```
python --version
```
Same Python you set up in `01_python_setup.md` — VS Code uses it automatically.

---

## Step 4 – Create and run your first file in VS Code

1. In the Explorer panel, click the **New File** icon (or right-click → New File)
2. Name it `hello.py`
3. Type this in the editor:

```python
print("VS Code is working!")
print("Python is running on my machine.")
```

4. Save: `Ctrl + S`
5. In the terminal at the bottom, type:
```
python hello.py
```
Press Enter. You should see your output.

---

## Step 5 – VS Code keyboard shortcuts to learn now

These will save you hours over the course:

| Shortcut | Action |
|---|---|
| `Ctrl + S` | Save file |
| `Ctrl + \`` | Open/close terminal |
| `Ctrl + /` | Comment or uncomment a line |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + P` | Command Palette — search for any VS Code action |
| `Alt + Up/Down` | Move a line of code up or down |
| `Ctrl + D` | Select next occurrence of selected word |

Try `Ctrl + Shift + P` and type "color theme" — you can change VS Code's appearance.

---

## Step 6 – Explorer tasks

Do each of these inside VS Code (no file explorer, no right-click on Desktop):

1. Create a new folder inside `python102` called `week1`
2. Inside `week1`, create a file called `practice.py`
3. Write 3 print statements in it — anything you want
4. Run it from the terminal:
```
cd week1
python practice.py
```
5. Edit one of the print statements, save, run again

---

## ✅ Checklist before moving on

- [ ] VS Code is installed and open
- [ ] You can see the Explorer, terminal, and status bar
- [ ] You created and ran `hello.py` from the VS Code terminal
- [ ] You know at least 4 keyboard shortcuts
- [ ] You created the `week1` folder and ran `practice.py`

Once all done, open `03_extensions.md`.
