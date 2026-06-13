# 04 – Python Programs
# Math+Coding Academy | Python102
#
# You already know: variables, input/output, if/elif/else,
# for loops, while loops, functions, basic Turtle.
#
# This file uses all of that — but now you're running it
# in a real environment with VS Code and a local Python install.
#
# Work through each program. Read the comments, run the code,
# then try the challenge at the end of each one.

# ===========================================================
# PROGRAM 1 – Number guessing game (review + refinement)
# ===========================================================
# You may have built something like this in Python101.
# Look at how it's structured here: one function per job,
# clear variable names, no repeated code.

import random

def get_guess():
    """Ask the user for a number between 1 and 100."""
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("That's not a number. Try again.")

def play_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("\n=== Number Guessing Game ===")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempt(s).")
            break

play_guessing_game()

# CHALLENGE: Add a difficulty setting at the start.
# Easy = 10 attempts max, Medium = 7, Hard = 5.
# If the player runs out of attempts, print the secret number.

# ===========================================================
# PROGRAM 2 – Text analyser
# ===========================================================
# This one uses string methods you haven't seen before.
# Read the comments carefully.

def analyse_text(text):
    """Return basic stats about a string."""
    word_count = len(text.split())          # split() breaks string into a list of words
    char_count = len(text)                  # total characters including spaces
    char_no_spaces = len(text.replace(" ", ""))  # characters without spaces
    sentence_count = text.count(".") + text.count("!") + text.count("?")

    print(f"\n=== Text Analysis ===")
    print(f"Words:       {word_count}")
    print(f"Characters:  {char_count}")
    print(f"Without spaces: {char_no_spaces}")
    print(f"Sentences:   {sentence_count}")
    print(f"Uppercase:   {text.upper()}")

user_text = input("\nEnter a sentence to analyse: ")
analyse_text(user_text)

# CHALLENGE: Add a function that counts how many times
# each vowel (a, e, i, o, u) appears in the text.
# Print the result like:
#   a: 3
#   e: 5
#   i: 1
#   o: 2
#   u: 0

# ===========================================================
# PROGRAM 3 – FizzBuzz (but make it a function)
# ===========================================================
# Classic programming problem. If you've seen it before,
# focus on how it's written here — not just that it works.

def fizzbuzz(n):
    """Print FizzBuzz from 1 to n."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

limit = int(input("\nRun FizzBuzz up to what number? "))
fizzbuzz(limit)

# CHALLENGE: Modify fizzbuzz() to return a LIST of results
# instead of printing them. Then print the list.
# Hint: create an empty list before the loop, append to it,
# and return it after. You'll need this skill next week.

# ===========================================================
# PROGRAM 4 – Grade calculator
# ===========================================================
# Demonstrates functions with return values, a loop,
# and building up a result over multiple inputs.

def letter_grade(score):
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_grades():
    """Ask the user to enter grades until they type 'done'."""
    scores = []
    print("\nEnter your grades one at a time. Type 'done' when finished.")

    while True:
        entry = input("Grade: ")
        if entry.lower() == "done":
            break
        try:
            score = float(entry)
            scores.append(score)
        except ValueError:
            print("Enter a number or 'done'.")

    return scores

def summarise_grades(scores):
    if not scores:
        print("No grades entered.")
        return

    average = sum(scores) / len(scores)
    print(f"\n=== Grade Summary ===")
    print(f"Grades entered: {len(scores)}")
    print(f"Highest:        {max(scores)}")
    print(f"Lowest:         {min(scores)}")
    print(f"Average:        {average:.1f}")
    print(f"Letter grade:   {letter_grade(average)}")

grades = get_grades()
summarise_grades(grades)

# CHALLENGE: Add a function that prints a simple bar chart
# of the grades. For each grade, print that many # symbols.
# Example for grade 85:
#   85 | #################################################################################
# Scale it: print one # per point.
