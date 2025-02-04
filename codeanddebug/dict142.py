# Ask subject name and marks from the user and keep adding
# it to dictionary
"""
Emaple = 
input =
Enetr the number of subject : 3
Enetr the subject name : maths
Enetr the marks for maths : 95
Enetr the subject name : english
Enetr the marks for english : 72 
Enetr the subject name : computer
Enetr the marks for computer : 80 

output =
{'maths': 95,'english': 95,'computer': 95}"""

sub = int(input("Enter the number of subject :"))
result = {}
for _ in range(sub):
    sub_name = input("Enter the subject name :")
    sub_marks = int(input(f"Enter the marks for {sub_name} : "))
    # result[sub_name] = sub_marks
    result.update({sub_name: sub_marks})

print(result)
