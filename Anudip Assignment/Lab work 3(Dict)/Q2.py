# Question 2: Student and grade dictionary

# Creating a dictionary to store students and their grades
student_grades = {
    "John": "A",
    "Emma": "B",
    "Mike": "A",
    "Sophia": "C"
}

# Printing the entire dictionary
print("Student Grades:", student_grades)

# Accessing the grade of a specific student (e.g., John)
print("Grade of John:", student_grades["John"])

# Adding a new student and their grade
student_grades["Oliver"] = "B"
print("Updated Student Grades:", student_grades)

# Updating the grade of an existing student
student_grades["Sophia"] = "B"
print("Updated Grade of Sophia:", student_grades["Sophia"])

# Deleting a student from the dictionary
del student_grades["Mike"]
print("Student Grades after deletion:", student_grades)
