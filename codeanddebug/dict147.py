"""
store name of student as key,"list of 5 marks" of that student
as a value.Store atleast 5 student names.print the sum and
percentage of all the students

"""

student_data = {
    "a": [85, 96, 42, 35, 45],
    "b": [95, 93, 72, 85, 45],
    "c": [45, 62, 55, 62, 51],
    "d": [75, 46, 46, 65, 12],
    "e": [62, 91, 62, 82, 65],
}
for name, marks in student_data.items():
    total = sum(marks)
    per = total / 500 * 100
    print(f"{name} got the total marks : {total} and percentage :{per:.2f}")
