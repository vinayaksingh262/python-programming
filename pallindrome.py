"""def is_pallindrome(string):
    return string == string[::-1]


text = input("")
if is_pallindrome(text):
    print("yes")
else:
    print("no")"""


def is_pallindrome(n):
    num = str(n)
    return num == num[::-1]


number = int(input(""))
if is_pallindrome(number):
    print("yes")
else:
    print("no")
