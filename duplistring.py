def duplicate_string(string):
    duplicate = []
    for char in set(string):
        if string.count(char) > 1:
            duplicate.append(char)
    return duplicate


string = input("enter string:")
print("duplicate items:", duplicate_string(string))
