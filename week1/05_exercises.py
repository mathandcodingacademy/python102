# 05 – Week 1 Exercises
# Math+Coding Academy | Python102
#
# These are your independent exercises for Week 1.
# You have everything you need from Python101 + what we covered today.
# Run your file often. Read error messages carefully.
# When you're done, push to GitHub.

# ===========================================================
# EXERCISE 1 – Rock, Paper, Scissors
# ===========================================================
# Build a complete Rock, Paper, Scissors game against the computer.
#
# Requirements:
# - Player enters their choice (rock, paper, or scissors)
# - Computer picks randomly using random.randint or random.choice
# - Print who won and why (e.g. "Rock beats Scissors — you win!")
# - Handle invalid input (if player types something other than the 3 options)
# - Ask if the player wants to play again after each round
# - Track and display total wins, losses, and ties when the player quits
#
# Structure your code with at least these functions:
#   get_player_choice()   → returns the player's valid choice
#   get_computer_choice() → returns a random choice
#   determine_winner(player, computer) → returns "win", "lose", or "tie"
#   play_game()           → runs the full game loop

import random

# YOUR CODE HERE


# ===========================================================
# EXERCISE 2 – Word counter
# ===========================================================
# Write a program that asks the user to type a paragraph (one long input).
# Then print:
#   - Total word count
#   - The longest word
#   - The most common word (and how many times it appears)
#   - How many words are longer than 5 characters
#
# Hints:
#   text.split()          → list of words
#   word.lower()          → lowercase so "The" and "the" count as the same
#   len(word)             → length of a word
#
# Structure your solution with functions — one function per task above.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 3 – Times table tester
# ===========================================================
# Build a times table quiz.
#
# Requirements:
# - Ask the player which times table they want to practice (e.g. 7)
# - Ask 10 questions in random order (e.g. "7 x 4 = ?")
# - Tell them if each answer is correct or wrong
# - At the end, show their score (e.g. "8 out of 10")
# - If they score less than 7, offer to play again
#
# Use random.sample or random.randint to vary the questions.
# Use functions to keep your code organized.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 4 (Bonus) – Caesar cipher
# ===========================================================
# A Caesar cipher shifts each letter in a message by a fixed number.
# Example with shift of 3:
#   "hello" → "khoor"
#   A→D, B→E, C→F ... Z→C (wraps around)
#
# Build an encoder AND decoder.
#
# Requirements:
# - Ask the user: encode or decode?
# - Ask for the message
# - Ask for the shift number (1-25)
# - Print the result
# - Only shift letters — leave spaces, numbers, punctuation unchanged
# - Handle both uppercase and lowercase
#
# Hints:
#   ord("a")        → 97 (ASCII code for 'a')
#   chr(97)         → "a" (character from ASCII code)
#   (x % 26)        → wraps around the alphabet
#   "A".isupper()   → True
#   "a".islower()   → True
#   "5".isalpha()   → False

# YOUR CODE HERE
