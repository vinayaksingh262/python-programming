"""
generate a list of 10 elements ,then create a two list one is odd and second one is even
"""

my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
even = []
odd = []
for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
