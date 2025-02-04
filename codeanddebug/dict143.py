# convert two list into a dictionary.
"""EXAMPLE
lst1=['ten','twenty','thirty']
lst2=[10,20,30]

{'ten' :10,'twenty':20,'thirty':30} """

lst1 = ["ten", "twenty", "thirty"]
lst2 = [10, 20, 30]
result = {}

for i in range(len(lst1)):
    result[lst1[i]] = lst2[i]
print(result)
