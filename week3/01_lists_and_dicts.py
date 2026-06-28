# 01 – Lists and Dictionaries
# Math+Coding Academy | Python102
#
# You already know: variables, input/output, if/elif/else,
# for loops, while loops, functions, and how to use Git/GitHub
# to save your work.
#
# Until now, every variable has held ONE thing: one number,
# one string, one True/False. This week you learn two new
# data structures that hold MANY things at once:
#
#   LIST       — an ordered collection. Use it when order/position matters
#                or you just need "a bunch of things."
#   DICTIONARY — a collection of key -> value pairs. Use it when you need
#                to look something up by name instead of by position.
#
# Remember the FizzBuzz challenge from Week 1, where you were asked to
# build a list inside a loop using .append()? That was a preview of
# today. Now we go deeper.
#
# Work through each program. Run it, change the values, see what breaks.

# ===========================================================
# PROGRAM 1 – Lists: storing a collection
# ===========================================================
# A list is created with square brackets. Items are separated by commas.
# Each item has a position called an INDEX, starting at 0 (not 1).

students = ["Amelia", "Noah", "Priya", "Tariq"]

print("Full list:", students)
print("First student (index 0):", students[0])
print("Last student (index -1):", students[-1])
print("How many students:", len(students))

# Lists are MUTABLE — you can change them after creating them.
students.append("Wei")          # adds to the end
print("After append:", students)

students[1] = "Noah K."         # overwrite by index
print("After renaming index 1:", students)

students.remove("Tariq")        # removes by value, not index
print("After remove:", students)

# CHALLENGE: Create a list called colours with 4 colour names.
# Print the 2nd colour using its index. Then append a 5th colour
# and print the full updated list.

# ===========================================================
# PROGRAM 2 – Iterating over a list
# ===========================================================
# "Iterating" just means looping over every item, one at a time.
# This is the #1 thing you'll do with lists.

def print_roster(names):
    """Print every name in the list with a number in front."""
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

print("\n=== Class Roster ===")
print_roster(students)

# You can also loop over a list to calculate things — just like the
# grade calculator from Week 1, but now the grades are stored properly
# in a list from the start instead of being typed in one at a time.

def class_average(scores):
    """Return the average of a list of numbers."""
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

grades = [88, 91, 76, 95, 82]
print(f"\nGrades: {grades}")
print(f"Average: {class_average(grades):.1f}")
print(f"Highest: {max(grades)}")
print(f"Lowest:  {min(grades)}")

# CHALLENGE: Write a function count_passing(scores, passing_grade)
# that loops over the list and returns how many scores are
# greater than or equal to passing_grade. Test it on `grades` with 80.

# ===========================================================
# PROGRAM 3 – Dictionaries: storing key -> value data
# ===========================================================
# A list finds things by POSITION (index 0, 1, 2...).
# A dictionary finds things by NAME (a "key"), which is often
# more useful — you don't need to remember an item's position.

student = {
    "name": "Priya",
    "grade": 7,
    "favourite_subject": "Coding"
}

print("\n=== Student Record ===")
print("Full dictionary:", student)
print("Name:", student["name"])
print("Grade:", student["grade"])

# Dictionaries are mutable too.
student["favourite_subject"] = "Math"   # change an existing value
student["email"] = "priya@example.com"  # add a brand-new key
print("After updates:", student)

# Looking up a key that doesn't exist crashes your program:
#   print(student["locker_number"])   # KeyError!
#
# .get() looks it up SAFELY and returns a default instead of crashing:
print("Locker number:", student.get("locker_number", "Not assigned"))

# CHALLENGE: Create a dictionary called book with keys "title",
# "author", and "pages". Print a sentence using all three values
# in one f-string, e.g. "Wonder by R.J. Palacio, 315 pages."

# ===========================================================
# PROGRAM 4 – Iterating over a dictionary
# ===========================================================
# Three ways to loop over a dictionary: keys, values, or both at once.

inventory = {
    "pencils": 24,
    "notebooks": 10,
    "erasers": 15,
    "rulers": 8
}

print("\n=== Inventory: keys only ===")
for item in inventory.keys():
    print(item)

print("\n=== Inventory: values only ===")
for count in inventory.values():
    print(count)

print("\n=== Inventory: keys AND values ===")
for item, count in inventory.items():
    print(f"{item}: {count}")

# Classic real use of dictionaries: counting things.
# Remember the text analyser from Week 1? Here's the upgrade —
# instead of only counting vowels, we count EVERY word automatically.

def word_frequency(text):
    """Return a dictionary of {word: how many times it appears}."""
    counts = {}
    for word in text.lower().split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
freq = word_frequency(sentence)
print(f"\n=== Word Frequency ===")
for word, count in freq.items():
    print(f"{word}: {count}")

# CHALLENGE: Write a function most_common_word(freq_dict) that loops
# over the dictionary and returns the word with the highest count.
# Hint: keep track of the best word and best count seen so far,
# the same pattern you used for max() logic in earlier weeks.

# ===========================================================
# PROGRAM 5 – Lists of dictionaries (the real combo)
# ===========================================================
# In real programs, you almost never store ONE student or ONE item.
# You store a LIST of dictionaries — one dictionary per record.
# This is exactly how data looks in spreadsheets, databases, and
# the files you'll learn to save next week.

class_records = [
    {"name": "Amelia", "grade": 88},
    {"name": "Noah",   "grade": 73},
    {"name": "Priya",  "grade": 95},
    {"name": "Tariq",  "grade": 67},
    {"name": "Wei",    "grade": 82},
]

print("\n=== Full Class Records ===")
for record in class_records:
    print(f"{record['name']}: {record['grade']}")

def students_above(records, minimum):
    """Return a list of names whose grade is >= minimum."""
    names = []
    for record in records:
        if record["grade"] >= minimum:
            names.append(record["name"])
    return names

honours = students_above(class_records, 85)
print(f"\nStudents with 85+: {honours}")

# CHALLENGE: Write a function class_average(records) that loops over
# class_records, pulls out each "grade" value, and returns the average.
# This is the same logic as PROGRAM 2 — but now the numbers live
# inside dictionaries instead of a plain list.
#
# Save this thought: next week you'll learn to write class_records
# to a file so it doesn't disappear every time you close VS Code.
