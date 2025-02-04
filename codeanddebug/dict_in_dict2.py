"""
vinayak -> 234(total marks)
xyz ->666
pqr-> 656
"""

student_data = {
    "vinayak": {
        "roll_no": 65,
        "gender": "male",
        "age": 21,
        "physics": 80,
        "chemistry": 84,
        "maths": 93,
    },
    "xyz": {
        "roll_no": 63,
        "gender": "male",
        "age": 22,
        "physics": 80,
        "chemistry": 74,
        "maths": 68,
    },
    "pqr": {
        "roll_no": 61,
        "gender": "male",
        "age": 22,
        "physics": 75,
        "chemistry": 94,
        "maths": 68,
    },
}
for name, details in student_data.items():

    total = details["physics"] + details["chemistry"] + details["maths"]
    print(f"{name} -> {total}")
