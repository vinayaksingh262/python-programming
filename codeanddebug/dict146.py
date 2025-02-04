# ask astring from user.display the dictionary where each key is a character and vale is the frequency of that character that comes in that string..
str = input("Enter a string:")
result = {}
for ch in str:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1

print(result)
