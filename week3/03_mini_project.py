# 03 – Mini Project: Class Grade Tracker
# Math+Coding Academy | Python102
#
# Everything before this was practice in isolation. This is one real,
# complete program that uses lists AND dictionaries together, the way
# an actual application would.
#
# THE BRIEF
# ---------
# Build a command-line app that tracks students and their grades.
#   - A "roster" is a LIST.
#   - Each student in the roster is a DICTIONARY: {"name": ..., "grades": [...]}
#   - Each student's grades are themselves a LIST, stored inside their dictionary.
#
# That's three of this week's ideas nested inside each other — exactly
# how real data looks (this is basically what a JSON file or a database
# table full of student records looks like).
#
# THE MENU LOOP (bottom of this file) is already built for you, so you
# can run this file right now and use the menu — it just won't DO
# anything yet, because the 5 functions above it are empty. Your job
# is to fill in those 5 functions. Don't touch the menu loop.
#
# Test as you go: implement add_student, run the file, choose option 1,
# then option 4, and check the roster looks right before moving on.

# ===========================================================
# PART 1 – Add a student
# ===========================================================
def add_student(roster, name):
    """
    Add a new student to the roster.
    Each student should be added as a dictionary in this exact shape:
        {"name": name, "grades": []}
    (an empty list — they have no grades yet)
    """
    # YOUR CODE HERE
    pass


# ===========================================================
# PART 2 – Find a student
# ===========================================================
def find_student(roster, name):
    """
    Search the roster for a student with this name (case-insensitive,
    so "priya" finds "Priya"). Return their dictionary if found,
    otherwise return None.

    Hint: loop over roster, compare record["name"].lower() to name.lower()
    """
    # YOUR CODE HERE
    pass


# ===========================================================
# PART 3 – Add a grade for a student
# ===========================================================
def add_grade(roster, name, grade):
    """
    Find the student by name (use find_student — don't search again
    from scratch) and append the new grade to their "grades" list.
    If the student doesn't exist, print a message instead of crashing.
    """
    # YOUR CODE HERE
    pass


# ===========================================================
# PART 4 – One student's average
# ===========================================================
def student_average(student):
    """
    Given ONE student dictionary, return the average of their grades.
    Return 0 if they have no grades yet — don't divide by zero!
    """
    # YOUR CODE HERE
    pass


# ===========================================================
# PART 5 – Class summary
# ===========================================================
def class_summary(roster):
    """
    Print every student's name and their average grade.
    Then print:
      - the name of the student with the highest average
      - the overall class average across every student

    If the roster is empty, print a message instead of crashing.
    """
    # YOUR CODE HERE
    pass


# ===========================================================
# THE MENU — already built. Read it, but you shouldn't need to
# change it. It just calls the 5 functions above.
# ===========================================================
def main():
    roster = []

    while True:
        print("\n=== Class Grade Tracker ===")
        print("1. Add student")
        print("2. Add grade")
        print("3. View one student's average")
        print("4. View class summary")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            add_student(roster, name)
            print(f"Added {name}.")

        elif choice == "2":
            name = input("Student name: ")
            grade = float(input("Grade: "))
            add_grade(roster, name, grade)

        elif choice == "3":
            name = input("Student name: ")
            student = find_student(roster, name)
            if student:
                print(f"{student['name']}'s average: {student_average(student):.1f}")
            else:
                print("Student not found.")

        elif choice == "4":
            class_summary(roster)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()

# ===========================================================
# STRETCH GOALS (once the menu fully works)
# ===========================================================
# - Don't allow the same name to be added twice. add_student should
#   check find_student first and refuse (or warn) if the name exists.
# - Add a 6th menu option: "Remove a student."
# - In class_summary, print students sorted from highest average to
#   lowest, not just in the order they were added.
# - Add a "subject" key to each student's dictionary and let
#   class_summary group/report by subject.
#
# Keep this file around — next week (File I/O) you'll learn to save
# this exact `roster` list of dictionaries to a file, so your class
# data survives after you close VS Code instead of disappearing.
