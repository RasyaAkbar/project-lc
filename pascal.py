row = int(input("Input your pascal row: "))
pascal_row = [1]
prev_val = 1
for column in range(1, row):
    next_val = prev_val * (row - column) // column
    pascal_row.append(next_val)
    prev_val = next_val
print(pascal_row)
