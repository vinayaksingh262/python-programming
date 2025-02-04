"""
WAP that prompts the user to specify the length of a list and then requests numbers to populate that list.
Display the final lsit as output """

lenght_list = int(input("Enter the length of a list:"))
result = []
for i in range(0, lenght_list):
    num = int(input("Enter the value:"))
    result.append(num)
print(result)
