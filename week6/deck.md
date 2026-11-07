# Python102 — Week 6
## Introduction to AI + Using AI Tools in VS Code

---

## 🤖 What Even IS Artificial Intelligence?

Not this: 🦾 robots taking over the world  
Not this: ✨ magic that knows everything

**This:** a program that learns patterns from examples — instead of being told every rule

> Traditional program: you write every rule  
> AI program: you show it thousands of examples, it figures out the rules itself

---

## 🧠 Traditional Programming vs Machine Learning

| Traditional | Machine Learning |
|-------------|-----------------|
| You write rules: `if temp > 30: print("hot")` | You show examples: 10,000 weather readings labelled "hot" or "cold" |
| Program does exactly what you told it | Program figures out the rule from the data |
| Adding new cases = rewriting rules | Adding new cases = retrain with more data |
| Great when rules are clear | Great when rules are too complex to write |

> **Both are just Python.** ML is not a different language — it's a different way of solving problems.

---

## 📚 What Does "Training" Actually Mean?

1. You collect **labelled examples** — photos of cats labelled "cat", dogs labelled "dog"
2. You feed them into a **model** (a mathematical function with millions of adjustable numbers)
3. The model makes a guess → checks if it's right → adjusts its numbers → repeat millions of times
4. After training: the model's numbers are locked. Now it can guess on *new* photos it's never seen

> You did this in Week 9-10 of this course with Teachable Machine — that IS training.  
> You took photos, labelled them, clicked Train. That's it.

---

## 🗂️ Types of AI Models (Just the Names for Now)

| Type | What it does | Example |
|------|-------------|---------|
| **Classification** | "Which category is this?" | Spam or not spam? Cat or dog? |
| **Regression** | "What number will this be?" | What will this house sell for? |
| **Generation** | "Create something new" | Write a sentence, draw an image |
| **Recommendation** | "What might you like?" | Netflix next-up, Spotify Discover |

> The trash sorter (week 9-10) is **classification**: which bin does this belong in?  
> GitHub Copilot is **generation**: given your comment, write the next lines of code.

---

## 📱 AI You Already Use Every Day

- **Autocorrect** — predicts the right word from millions of text examples
- **Face unlock** — classifies: is this face the owner's face?
- **Spotify / YouTube recommendations** — trained on what you've listened to / watched
- **Google Search ranking** — predicts which page you actually want
- **Spam filter** — classifies each email as spam or not
- **ChatGPT / Copilot** — generates text trained on most of the internet

> None of these were programmed with hand-written rules.  
> All of them learned patterns from enormous amounts of data.

---

## 💬 What Is a Large Language Model (LLM)?

An LLM is a model trained on **enormous amounts of text** — books, websites, code, articles.

It learned one thing: *given text so far, what word comes next?*  
Do that millions of times fast enough → it can write, explain, code, answer questions.

```
You type:    "Write a Python function that adds two numbers"
LLM thinks:  "what text comes after this, based on everything I've seen?"
LLM writes:  def add(a, b):
                 return a + b
```

> It does NOT look things up. It does NOT think. It **predicts likely next tokens**.  
> This is why it can sound very confident and still be completely wrong.

---

## 🛠️ GitHub Copilot — Your AI Pair Programmer

Copilot is an LLM (made by GitHub + OpenAI) trained specifically on public code.

**Three ways to use it:**

| Mode | How |
|------|-----|
| **Inline suggestion** | Write a comment describing what you want → Copilot suggests the code → Tab to accept |
| **Copilot Chat** | Open the chat panel → ask questions, explain code, fix bugs |
| **Edit / refactor** | Select code → ask Copilot to rewrite, simplify, or add error handling |

> **In this course we use VS Code.** Some of you have GitHub Copilot built in; some
> use other AI tools like Gemini alongside VS Code. They all work the same way:
> you describe what you want, the AI suggests code, you read it before you accept it.

---

## 🖱️ How to Open Copilot Chat in VS Code

Three ways — pick whichever you see:

| Way | How |
|-----|-----|
| **Click the icon** | Chat / speech-bubble icon at the top of the VS Code window |
| **Use the menu** | `View` → `Chat` → `Open Chat` |
| **Keyboard shortcut** | `Ctrl+Alt+I` (Windows/Linux) · `Ctrl+Cmd+I` (Mac) |

> First time? You may see **"Sign in to GitHub"** — click it, approve in your
> browser, then come back to VS Code.
>
> No chat icon at all? The extension isn't installed: open **Extensions**
> (`Ctrl+Shift+X`) → search **"GitHub Copilot Chat"** → **Install**.

---

## 🎯 The Golden Rule: YOU Are the Senior Developer

AI-generated code is a **first draft from a junior developer** — not a finished answer.

Your job every time:
1. ✅ Read it line by line before you run it
2. ✅ Understand what each line does — or ask the AI to explain it
3. ✅ Test it with at least one input you expect to work AND one you expect to break
4. ✅ If you can't explain it, you don't own it yet

> The AI can write code that *looks* right, runs without errors, and gives the *wrong* answer.  
> Only you can catch that — because only you know what the right answer actually is.

---

## 💡 Prompting 101 — How to Talk to an AI Coding Tool

**Bad prompt** → vague → bad code:
> "make a function"

**Better prompt** → specific → better code:
> "Write a Python function called `calculate_average(scores)` that takes a list of numbers and returns their average. If the list is empty, return 0."

**Three ingredients of a good prompt:**
1. **What** — function, class, fix, explanation?
2. **Inputs and outputs** — what goes in, what comes out?
3. **Edge cases** — what should happen if the input is weird?

---

## ⚠️ AI Can Be Wrong — and It Won't Tell You

Common ways Copilot / ChatGPT gets it wrong:

| Problem | What happens |
|---------|-------------|
| **Hallucination** | Invents a function that doesn't exist — code looks right but crashes |
| **Off-by-one** | Gets loop ranges slightly wrong |
| **Wrong edge case** | Handles the normal case fine, crashes on empty list / zero / None |
| **Outdated info** | Uses an old library version or deprecated function |
| **Security holes** | Writes code that works but can be exploited |

> This is why we test everything ourselves. The AI doesn't run your program — you do.

---

## 🗓️ What We'll Build With AI (Weeks 7–12)

| Weeks | Project | AI role |
|-------|---------|---------|
| 7–8 | 🌦️ Weather Mood App | Copilot writes the API + GUI code; you drive, read, and test |
| 9–10 | 🗑️ Trash Sorter | You train the model; Copilot writes the webcam app |
| 11–12 | 🚀 TBD | TBD |

> The AI writes a lot of the code — that's the point.  
> **Your job is to understand and control what it writes.**

---

## ✅ Check In Before We Open VS Code

1. In your own words: what's the difference between *traditional programming* and *machine learning*?
2. What does "training a model" mean? (don't just say "the computer learns stuff")
3. Name one thing Copilot is good at and one thing you should always check yourself.

> If you can answer all three → open VS Code, let's use the thing.
