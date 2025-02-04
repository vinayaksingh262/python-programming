"""
in given list prompted the user for an old nmber followed by anew number .
if the old number exist in the list ,replace with it the new number provided by the user"""

my_list = [5, 10, 15, 20, 15]
old, new = 15, 25
for i in range(0, len(my_list)):
    if my_list[i] == old:
        my_list[i] = new
print(my_list)
