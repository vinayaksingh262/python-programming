# wap to ask a string from a user.Count how many alphabates are there in that string

# method 1
x = "vinayak26"
count = 0
for i in x:
    if i.isalpha():
        count = count + 1
print(count)

# method 2
x = "VSR26"
count = 0
for i in x:
    ascii = ord(i)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1
print(count)
