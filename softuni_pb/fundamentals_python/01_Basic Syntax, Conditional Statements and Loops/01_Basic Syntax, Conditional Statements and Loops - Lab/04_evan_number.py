
for i in range(int(input())):
    num = int(input())
    if not num % 2 == 0:  # if num % 2 != 0:
        print(f"{num} is odd!")
        break
else:
    print("All numbers are even.")


