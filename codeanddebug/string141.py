""" WAP that converts a string in camelCase to snake_case
for example- "helloWorldHowAreYou"
             "hello_world_how_are_you"""

str = "helloWorldHowAreYou"

# method 1


result = "".join(["_" + i.lower() if i.isupper() else i for i in str])

print(result)

# method 2


snake = ""
for char in str:
    if str.isupper():
        snake += "_" + str.lower()
    else:
        snake += char
print(result)
