'''
enter n=8
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6
7 7 7 7 7
8 8 8 8 8
'''
n=int(input("Enter n ="))
for i in range(1,n+1):
    for j in range(1,6):
        print(i,end=" ")
    print()