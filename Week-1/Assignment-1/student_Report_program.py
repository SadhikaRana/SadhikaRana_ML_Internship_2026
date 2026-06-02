# 7. Create a Student Report Program that take student details using input(), store marks in variables, calculate total and percentage. use comments and proper identation.

# Student Report Program
# Taking student details
student_name = input("Enter student name:")
student_age = int(input("Enter student age:"))
student_class = input("Enter student class:")

# Taking marks in subjects
math_marks = float(input("Enter marks in Mathematics:"))
science_marks = float(input("Enter marks in Science:"))
english_marks = float(input("Enter marks in English:"))
# Calculating total marks and percentage
total_marks = math_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100

# Displaying the report
print("\nStudent Report")
print("Name:", student_name)
print("Age:", student_age)
print("Class:", student_class)
print("Mathematics:", math_marks)
print("Science:", science_marks)
print("English:", english_marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage)