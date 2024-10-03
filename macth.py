x=4
match x:
    case 0:
        print("x is zero")
    case 4 if x%2==0:
        print("x%2==0 and case 4")
    case _ if x<10:
        print("x is < 10")
    case _:
        print(x)

