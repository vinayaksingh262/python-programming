# WAP that reverse each word in a sentence while maintaining the word order
# for example- "hello world"
#             "olleh dlrow"

mystring = "hello world"
x = mystring.split()
str = " ".join(i[::-1] for i in x)
print(str)
