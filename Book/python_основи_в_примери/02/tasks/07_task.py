"""""""""ЗАДАЧА 7  - стр. 130 """""""""

# Проверка дали трите последователно написани числа са аретмитична прогресия

numbers = [int(input("Въведете първо число: ")), int(input("Въведете второ число: ")), int(input("Въведете трето число: "))]

fixed_number = numbers[1] - numbers[0]

print("Yes, this is an arithmetic progression.") if numbers[2] - numbers[1] == fixed_number \
    else print("No, this is a not an  arithmetic progression ")


"""""""""ЗАДАЧА 6  - стр. 130 """""""""


# проверка дали сумата на 2 от страните е по-голяма на третата. Това е условие за построяване на триъгълник.

numbers = [int(input("Въведете първо число: ")), int(input("Въведете второ число: ")), int(input("Въведете трето число: "))]

can_form_triangle = False

# Проверка дали сумата на две числа от списъка е по-голяма от третото
len_numbers = len(numbers)
for i in range(len_numbers):
    for j in range(i + 1, 3):
        total = numbers[i] + numbers[j]
        if total > numbers[3 - i - j]:
            can_form_triangle = True
            break

print("Можете да построите триъгълник с тези числа.") if can_form_triangle == True \
    else print("Не можете да построите триъгълник с тези числа.")
