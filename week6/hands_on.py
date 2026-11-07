# Week 6 — Hands-On: Using AI Tools in VS Code
#
# This file is your practice ground for working WITH an AI coding tool.
# Use whatever you have set up in VS Code — GitHub Copilot, or another AI assistant.
#
# GROUND RULES FOR TODAY:
#   1. Don't just accept whatever the AI gives you — READ it first.
#   2. If you can't explain a line out loud, don't keep it yet. Ask the AI to explain it.
#   3. Every piece of AI code gets TESTED by you before you move on.

# ============================================================
# ACTIVITY 1: Inline Suggestions (10 min)
# ============================================================
# HOW: Write the comment below, then STOP TYPING.
# Wait for your AI tool to suggest the function body.
# Press Tab to accept. Then READ every line before running.

# Write a function called celsius_to_fahrenheit that takes a
# temperature in Celsius and returns it in Fahrenheit.
# Formula: F = (C * 9/5) + 32


# --- After the AI writes it, answer these before running: ---
# Q1: What does the formula do step by step?
# Q2: What should celsius_to_fahrenheit(0) return?   → you say: ___
# Q3: What should celsius_to_fahrenheit(100) return? → you say: ___

# NOW run it and check your answers:
# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(100))
# print(celsius_to_fahrenheit(-40))   # -40°F = -40°C — a fun fact to verify!


# ============================================================
# ACTIVITY 2: Ask the AI to Explain Code You Don't Understand
# ============================================================
# Here is a function written by the AI. Read it.
# For any line you don't understand, highlight it and ask Copilot Chat:
# "Explain this line to me like I'm 12."

def most_common(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

# --- Before running, try to figure out: ---
# Q1: What does counts.get(item, 0) do? (Hint: what happens the first time we see an item?)
# Q2: What does max(counts, key=counts.get) do?
# Q3: What will most_common(["a", "b", "a", "c", "a", "b"]) return?  → you say: ___

# Run it and check:
print(most_common(["a", "b", "a", "c", "a", "b"]))

# Q4: What happens if you call most_common([]) ?  → predict first, then try it.
# (Does the AI's code handle this? If not, ask the AI to fix it — then read the fix.)


# ============================================================
# ACTIVITY 3: Prompt the AI with a Good Spec (10 min)
# ============================================================
# Write a detailed comment below, then let the AI generate the function.
# Use the 3-ingredient formula: WHAT + INPUTS/OUTPUTS + EDGE CASES.

# Write a Python function called word_count(text) that:
#   - Takes a string of text
#   - Returns a dictionary where each key is a word and the value is how many times it appears
#   - Words should be lowercased so "Hello" and "hello" count as the same word
#   - Ignore punctuation (commas, periods, exclamation marks)
#   - If the input is an empty string, return an empty dictionary


# --- After the AI writes it: ---
# Q1: How does it handle lowercasing?
# Q2: How does it handle punctuation? (What method/approach did it use?)
# Q3: Test it:

# print(word_count("Hello world hello"))          # {'hello': 2, 'world': 1}
# print(word_count("Hi! Hi, hi."))                # {'hi': 3}
# print(word_count(""))                           # {}


# ============================================================
# ACTIVITY 4: Find the Bug the AI Introduced (10 min)
# ============================================================
# The function below was written by an AI. It has a bug.
# Read it carefully, predict what it does, then run it.
# Find the bug WITHOUT asking the AI — use your own brain first.
# Only ask the AI for a hint if you're truly stuck after 5 minutes.

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

# Tests — some of these will crash or give wrong answers:
print(calculate_average([10, 20, 30]))    # should be 20.0 ✓
print(calculate_average([5]))             # should be 5.0  ✓
# print(calculate_average([]))            # what happens? uncomment and try

# --- After finding the bug: ---
# Fix it so calculate_average([]) returns 0 instead of crashing.
# Write your fix below — DON'T ask the AI yet. Try yourself first.


# ============================================================
# ACTIVITY 5: Use AI to Add a Feature (10 min)
# ============================================================
# Here is a simple Student class. It works fine.
# Your job: ask the AI (via Copilot Chat or inline) to add ONE feature.
# Then: read the new code, understand it, test it.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} | Average: {self.average():.1f}"


# Task: Ask the AI to add a method called letter_grade(self) that returns:
#   "A" if average >= 90
#   "B" if average >= 80
#   "C" if average >= 70
#   "D" if average >= 60
#   "F" otherwise
#
# Prompt to use (type it into Copilot Chat):
# "Add a method called letter_grade() to this Student class that returns
#  A/B/C/D/F based on the student's average grade."
#
# After the AI adds it:
# Q1: Does it match the thresholds above exactly?
# Q2: Test it:

s = Student("Alex")
s.add_grade(95)
s.add_grade(88)
s.add_grade(91)
print(s)
# print(s.letter_grade())   # uncomment after you add the method


# ============================================================
# WRAP-UP: Reflection (last 5 min, discuss with instructor)
# ============================================================
# 1. Which activity was hardest — writing the prompt, reading the code, or finding the bug?
# 2. In Activity 4, did the AI write bad code? What kind of mistake was it?
# 3. Going into the project weeks: what's ONE thing you'll always do before accepting AI code?
