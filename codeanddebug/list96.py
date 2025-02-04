# print sum of all elemnets in list

x = list(map(int, input("Enter the number seperated by space :").split()))
total = 0
for i in x:
    total = total + i
print("SUM OF ALL ELEMENTS: ", total)
