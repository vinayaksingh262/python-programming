x=int(input("Emter the value of x:"))
match x:
    case 0:
        print("x is zero")
    
    
    case _ if x<0:
        print(x," is negative")
    case _ :
        print(x)
