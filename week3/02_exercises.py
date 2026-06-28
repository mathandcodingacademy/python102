# 02 – Week 3 Exercises
# Math+Coding Academy | Python102
#
# These are your independent exercises for Week 3.
# Use everything from 01_lists_and_dicts.py — lists, dictionaries,
# looping with for, and looking up values with .get().
#
# Structure every exercise with functions. Run your file often.
# When you're done, add, commit, and push — same as Week 2.

# ===========================================================
# EXERCISE 1 – Grocery list manager
# ===========================================================
# Build a program that manages a shopping list using a list.
#
# Requirements:
# - Start with an empty list called grocery_list
# - Ask the user to type items one at a time, type "done" to stop
# - After each item is added, print the full updated list
# - Once they type "done", ask if they want to remove anything
#   (let them type an item name to remove, or "no" to skip)
# - Print the final list, the total number of items, and the
#   first and last item using index 0 and index -1
#
# Structure your code with at least these functions:
#   build_list()                    → returns the list after adding items
#   remove_items(grocery_list)      → removes items the user names
#   show_summary(grocery_list)      → prints count, first, and last item

# YOUR CODE HERE


# ===========================================================
# EXERCISE 2 – Contact book
# ===========================================================
# Build a simple contact book using a dictionary of dictionaries.
# Each contact is itself a dictionary with "phone" and "city".
#
# Example structure:
#   contacts = {
#       "Maya": {"phone": "555-0101", "city": "Moncton"},
#       "Eli":  {"phone": "555-0199", "city": "Halifax"}
#   }
#
# Requirements:
# - Pre-fill contacts with at least 3 people (use the example above as a guide)
# - Ask the user to type a name to look up
# - If the name exists, print their phone and city
# - If the name does NOT exist, print a friendly message —
#   do NOT let the program crash with a KeyError. Use .get().
# - Let the user add a new contact (name, phone, city) before quitting
# - Print the full, updated contact book at the end
#
# Structure your solution with functions — one per task above.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 3 – Class grade book
# ===========================================================
# Build a grade book using a LIST of DICTIONARIES, one dictionary
# per student, just like class_records in PROGRAM 5.
#
# Requirements:
# - Ask the user how many students to enter
# - For each student, ask for a name and a grade, and store them
#   as {"name": ..., "grade": ...} in a list
# - Print every student and their grade
# - Print the class average (use the same logic as class_average()
#   from PROGRAM 5, written from scratch yourself)
# - Print the names of every student who scored above the average
# - Print the name of the student with the highest grade
#   (don't just use max() on the whole record — you need the NAME
#   that goes with the highest grade)
#
# Hints:
#   records.append({"name": name, "grade": grade})
#   record["grade"]      → access a value inside one dictionary
#
# Structure your solution with functions — one per task above.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 4 (Bonus) – Word frequency, ranked
# ===========================================================
# Take the word_frequency() function from PROGRAM 4 further.
#
# Requirements:
# - Ask the user to type or paste a paragraph
# - Build the {word: count} dictionary (reuse or rewrite word_frequency)
# - Print every word and its count
# - Print the 3 most common words, from most to least common
#   (no need to use any new built-in functions — loop over the
#   dictionary repeatedly, find the current highest, print it,
#   then remove it from a working copy and repeat)
# - Print how many UNIQUE words were used (hint: len() on a dictionary
#   counts its keys)
#
# This is the same "find the biggest, repeat" pattern you used for
# most_common_word() in PROGRAM 4 — just looped 3 times instead of once.

# YOUR CODE HERE
