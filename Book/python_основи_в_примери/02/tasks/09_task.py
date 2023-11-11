"""""""""ЗАДАЧА 9  - стр. 131 """""""""

# Проверка при вход 2 числа кое числ ое по-голямо, да се използва тернарен оператор и обработка за изключителна ситуация.
"""""""""ЗА 2 числа """""""""

# try:
#     numbers = [int(input("Въведете първо число: ")), int(input("Въведете второ число: "))]
#
#     if numbers[0] == numbers[1]:
#         print("Двете числа са равни.")
#
#     print(f"{numbers[0]} е по-голямото число.") if numbers[0] > numbers[1] else print(f"{numbers[1]} е по-голямото число.")
#
#
# except ValueError:
#     print("Грешка: Въведете валидно цяло число.")

"""""""""ЗА n на брой числа """""""""
try:
    num_elements = int(input("Въведете брой на елементите в списъка: "))
    list_num = []

    for number in range(num_elements):
        number_input = int(input(f"Въведете число {number + 1}: "))
        list_num.append(number_input)

    if all(x == list_num[0] for x in list_num):
        print("Всички числа в списъка са равни.")
    else:
        max_num = max(list_num)
        print(f"{max_num} е най-голямото число в списъка.")

except ValueError:
    print("Грешка: Въведете валидно цяло число.")
