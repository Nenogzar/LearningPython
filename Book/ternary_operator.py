# стр. 111
num = int(input("start: "))
end = int(input("end:"))
a = 0
even_sum = 0
odd_sum = 0
for number in range(num, end + 1):
    # ternary operator
    res = "evan" if number % 2==0 else "odd"
    if res == "evan":
        even_sum += number
    else:
        odd_sum += number

print(f"the sum of the even numbers of {num} to {end} is: {even_sum}")
print(f"the sum of the odd numbers of {num} to {end} is: {odd_sum}")


