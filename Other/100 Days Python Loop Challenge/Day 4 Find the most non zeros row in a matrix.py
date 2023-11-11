                # Find the most non zeros row in a matrix
                # Определя се функцията non_zero(matrix), която приема матрица (списък от списъци) като аргумент.
def non_zero(matrix):
    max_count = 0
    max_row = None
                    # Ако броят на ненулевите елементи в текущия ред е по-голям от максималния брой ненулеви елементи,
                    # който е бил намерен до момента (max_count), програмата обновява max_count и записва текущия ред
                    # като "ред с най-много ненулеви елементи" (max_row).
    for row in matrix:
        count = sum(1 for elem in row if elem != 0)
        if count > max_count:
            max_count = count
            max_row = row
    return max_row



rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))
                    # След въвеждането, програмата извежда матрицата, като използва цикъл for,
                    # и след това извиква функцията non_zero(matrix).
matrix = []
print("\nEnter matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        while True:
            try:
                element = int(input(f"Enter element at position ({i}, {j}): "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        row.append(element)
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)
                    # Програмата въвежда броят на редовете и колоните на матрицата,
                    # след което въвежда елементите на матрицата чрез вложени цикли for.
result = non_zero(matrix)
print("\nRow with the most non-zero elements is:", result)

