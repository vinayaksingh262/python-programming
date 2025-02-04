# WAP to capatilize a first letter of each word while converting all other letters to lowercase

# method1

str = "hi vinayak how are you"
x = str.title()
print(x)

# method2

my_str = str.split()
x = " ".join(i.capitalize() for i in my_str)
print(x)
