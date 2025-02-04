my_lst = []
for i in range(1, 21):
    my_lst.append(i)
print(my_lst)

lst = [i for i in range(1, 21)]
print(lst)

lst1 = ["vinayak" for i in range(1, 5)]
print(lst1)

lst2 = ["even" if i % 2 == 0 else "odd" for i in range(1, 21)]
print(lst2)

# [2,4,6,....,28,30]
lst3 = [i for i in range(1, 31) if i % 2 == 0]
print(lst3)

my_lst1 = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]
print(my_lst1)
