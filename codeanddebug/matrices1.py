Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries row wise:")

for row in range(Row):
    a = []

    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)

for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()
