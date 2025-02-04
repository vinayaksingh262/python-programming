my_dict = {"maths": 88, "chemistry": 80, "physics": 84, "it": 94, "english": 72}
count = 0
for i in my_dict.keys():
    print(my_dict[i])
    count += my_dict[i]
print(count)
c = 0
for k in my_dict.values():
    c += k
print(c)
