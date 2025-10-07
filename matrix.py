row = int(input("Enter the size of row: "))
cols = int(input("Enter the size of column: "))
matrix = []


for i in range(row):
    rows = []
    for j in range(cols):
        val = int(input(f"Enter element at [{i}][{j}]: "))
        rows.append(val)
    matrix.append(rows)


print("\nMatrix is:")
for i in range(row):
    print(matrix[i])


x = int(input("\nEnter the number to be searched: "))
found = False

for k in range(row):
    for l in range(cols):
        if matrix[k][l] == x:
            print(f"Number found at position [{k}][{l}]")

