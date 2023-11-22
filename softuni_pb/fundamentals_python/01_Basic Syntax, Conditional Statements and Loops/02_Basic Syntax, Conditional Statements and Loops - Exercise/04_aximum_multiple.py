div = int(input())
bound = int(input())

for num in range(bound, div - 1, -1):
    if num % div == 0:
        break
print(num)

