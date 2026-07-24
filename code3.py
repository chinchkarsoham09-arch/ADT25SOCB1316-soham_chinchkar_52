# ==========================================
# Experiment 1: Types of Arguments in Python
# Name: soham
# Roll No:
# Division:
# ==========================================

# -------------------------------
# 1. Required Argument
# -------------------------------
def student(roll_no, name):
    print("Required Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)

student(1, "purva")


print("\n-------------------------------")

# -------------------------------
# 2. Keyword Argument
# -------------------------------
def student(roll_no, name):
    print("Keyword Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)

student(name="soham", roll_no=1)


print("\n-------------------------------")

# -------------------------------
# 3. Default Argument
# -------------------------------
def student(roll_no, name, division="A"):
    print("Default Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)
    print("Division:", division)

student(1, "soham")


print("\n-------------------------------")

# -------------------------------
# 4. Variable-Length Argument
# -------------------------------
def student(name, *subjects):
    print("Variable-Length Argument")
    print("Name:", name)
    print("Subjects:")
    for subject in subjects:
        print(subject)

student("soham", "Python", "Java", "HTML", "CSS")