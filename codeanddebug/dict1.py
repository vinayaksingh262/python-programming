# dictionary
x = {1: "vinayak", "age": 21, "marks": [10, 9, 8, 10], 2.3: [25, 30]}
print(x)
print(x["age"])
r = x.get(1)
print(r)
x.popitem()
print(x)
x.update({"mark": 99, "address": "bhopal"})
print(x)
