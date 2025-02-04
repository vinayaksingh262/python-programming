"""store name of student as key,"list of 5 marks" of that student
as a value.Store atleast 5 student.print name of the student who got highest marks
"""

student_data = {
    "student1": [85, 96, 42, 35, 45],
    "student2": [95, 93, 72, 85, 45],
    "student3": [45, 62, 55, 62, 51],
    "student4": [75, 46, 46, 65, 12],
    "student5": [62, 91, 62, 82, 65],
}
highest = 0
highest_name = ""
for name, marks in student_data.items():
    total = sum(marks)
    if total > highest:
        highest = total
        highest_name = name
print(f"student {highest_name} has gained highest marks...")
