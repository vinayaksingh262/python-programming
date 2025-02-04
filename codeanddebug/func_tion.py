def total_marks(physics, chemistry, maths, english, hindi=0):
    print(f"your marks in {physics}")
    print(f"your marks in {chemistry}")
    print(f"your marks in {maths}")
    print(f"your marks in {english}")
    print(f"your marks in {hindi}")
    total = physics + chemistry + maths + english + hindi
    print(f"your total marks is : {total}")


total_marks(physics=89, chemistry=90, maths=95, english=75)
