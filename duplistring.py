def find_duplicates(string):
    duplicates = []
    for char in set(string):
        if string.count(char) > 1:
            duplicates.append(char)
    return duplicates


string = "programming"
print("Duplicate items:", find_duplicates(string))
