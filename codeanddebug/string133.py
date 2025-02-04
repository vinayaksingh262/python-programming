# WAP to count the number of uppercase and lowercase of the string.
x = "Vinayak26SinghRajput"
lower, upper = 0, 0

# method1

for i in x:
    ascii = ord(i)

    if ascii >= 65 and ascii <= 90:
        upper += 1
    elif ascii >= 97 and ascii <= 122:
        lower += 1
print(f"count of lower case is {lower} and upper case is {upper}")

# method2

for i in x:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(upper, lower)
