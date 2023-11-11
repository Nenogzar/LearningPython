"""""""""ЗАДАЧА 2  - стр. 130 """""""""

# number = input("Enter a number: ")
#
# if number.isdigit():
#     complemented_number = ''.join(str(9 - int(digit)) for digit in number)
#     print(f"The complemented number is: {complemented_number}")
# else:
#     print("Enter a valid number.")

""""""""" ИЛИ """""""""
number = input("Enter a number: ")

while not number.isdigit():
    print("Enter an integer, not text: ")
    number = input("Enter a number: ")

else:
    complemented_number = ''
    for digit in number:
        complemented_number += str(9 - int(digit))
    print(f"The complemented number is: {complemented_number}")

