"""стр. 111"""
""" 1 """
# num = int(input("start: "))
# end = int(input("end:"))
#
# even_sum = 0
# odd_sum = 0
# for number in range(num, end + 1):
#
#     res = "evan" if number % 2==0 else "odd"
#     if res == "evan":
#         even_sum += number
#     else:
#         odd_sum += number
#
# print(f"the sum of the even numbers of {num} to {end} is: {even_sum}")
# print(f"the sum of the odd numbers of {num} to {end} is: {odd_sum}")

""" 2 """
# num, end = int(input("start: ")), int(input("end:"))
# even_sum, odd_sum = 0
#
# results = [("even", even_sum := even_sum + number) if number % 2 == 0 else ("odd", odd_sum := odd_sum + number) for number in range(num, end + 1)]
#
# print(f"the sum of the even numbers of {num} to {end} is: {even_sum}")
# print(f"the sum of the odd numbers of {num} to {end} is: {odd_sum}")

""" 3 """
num, end = int(input("start: ")), int(input("end:"))
even_sum = odd_sum = 0
results = [(("even", even_sum := even_sum + number)
				if
					number % 2 == 0
				else
					("odd", odd_sum := odd_sum + number))
				and
					number for number in range(num, end + 1)]

print(f"the sum of the even numbers from {num} to {end} is: {even_sum}")
print(f"the sum of the odd numbers from {num} to {end} is: {odd_sum}")