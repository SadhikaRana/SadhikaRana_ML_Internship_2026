# 5. Create Student Result System
#-	Input student details 
#-	Input marks 
#-	Calculate percentage 
#-	Display grade 
#-	Use: 
##loops 
#user input

# Student Result System
name_of_student = input("Enter Student Name: ")
roll_no_of_student = input("Enter Roll Number: ")
total_marks = 0
total_number_of_subjects = 5
for i in range(1, total_number_of_subjects + 1):
    marks = float(input("Enter marks for Subject:" + str(i) + ": "))
    total_marks += marks
percentage = total_marks / total_number_of_subjects
if percentage >= 93:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 77:
    grade = "B"
elif percentage >= 69:
    grade = "C"
elif percentage >= 61:
    grade = "D"
else:
    grade = "F"
print("\nSTUDENT RESULT")
print("Name:", name_of_student)
print("Roll Number:", roll_no_of_student)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
