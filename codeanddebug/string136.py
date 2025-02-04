# WAP to count the number of spaces in a string entered by user

my_string = "vin ayak singh"
count = 0
c = 0
for ch in my_string:
    if ch == " ":
        count += 1
print(count)
for i in my_string:
    if ord(i) == 32:
        c += 1
print(c)
