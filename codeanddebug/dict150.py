# WAP to combine two dictionary by adding values for common keys
d1 = {"a": 200, "b": 100, "c": 500}
d2 = {"a": 100, "b": 150, "x": 500}
result = {}
for k, v in d1.items():
    result[k] = v
for k, v in d2.items():
    if k in result:
        result[k] = result[k] + v
    else:
        result[k] = v
print(result)
