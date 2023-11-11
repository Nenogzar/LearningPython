evan_list = []
odd_list = []

for num in range(1, (int(input("дължината на списъците е до: ")))+1):
    evan_list.append(num) if pow(num, 1, 2) == 0 else odd_list.append(num)

print(evan_list)
print(odd_list)
