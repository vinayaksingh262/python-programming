one=int(input("Enter first number"))
two=int(input("Enter second number"))
three=int(input("Enter three number"))
if one==two or two==three or three==one:
    print("ERROR! entered number must be different...")
else:
    if one>two:
        if one>three:
          print(f"Numner {one} is greatest... ")
        else:
          print(f"Numner {three} is greatest... ")
    else:
        if two>three:
           print(f"number {two} is greater...")
        else:
           print(f"Number {three} is greater...")

