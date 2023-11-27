input_numbers = list(map(int, input().split()))
kill_step = int(input())
kill_step -= 1
n = len(input_numbers)
result, index = [], 0

for _ in range(n):
    index = (index + kill_step) % n
    eliminated_number = input_numbers.pop(index)
    result.append(str(eliminated_number))
    n -= 1

output = "[" + ",".join(result) + "]"
print(output)