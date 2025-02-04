# WAP to convert all string in uppercase
x = "vinayak"

# method1

y = x.upper()
print(y)

# method2

result = ""
for i in x:
    ascii = ord(i)
    if ascii >= 95 and ascii <= 127:
        new_ascii = ascii - 32
        char = chr(new_ascii)
        result += char
    else:
        result += i
print(result)
