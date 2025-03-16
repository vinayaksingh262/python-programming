# given two strings A and B,removes all characters in a that are presents in b and print the resulting string c

a = input().strip()
b = input().strip()
result = ""
for char in a:
    if char not in b:
        result += char
print(result)

a = input().strip()
b = input().strip()
result = "".join(char for char in a if char not in b)
print(result)
