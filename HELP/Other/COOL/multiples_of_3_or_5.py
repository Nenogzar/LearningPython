def solution(number):
    value = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
           value = value + i
    return value

print(solution(int(input("input range: "))))