n = int(input())  # Input the number of rows

for i in range(n):
    for j in range(i + 1):
        # Skip the second star in the third row (i = 2 and j = 1)
        if i == 2 and j == 1:
            print(" ", end="  ") # Print space instead of the star
        
        else:
            print("*", end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()