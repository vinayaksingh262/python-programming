"""WAP to find the occurance of each elements in the list and print the element of highest occurance."""

my_list = [5, 5, "vinayak", 5, 1, "vinayak"]
result = []
for i in my_list:
    if i not in result:
        result.append(i)

highest_occurance = 0
highest_occurance_ele = 0
for num in result:
    c = my_list.count(num)
    print(f"{num} occurs {c} times.")

    if c > highest_occurance:
        highest_occurance = c
        highest_occurance_ele = num
print(f"Highest occur element is : {highest_occurance_ele}")
