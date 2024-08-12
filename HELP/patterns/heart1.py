row = 7
for i in range(row):
    for j in range(row):
        if i == 0 and j % 3 != 0 or i == 1 and j % 3 ==0 or i-j == 2 or i +j == 8:
            print("*", end='')
        else:
            print(' ', end='')
    print()
