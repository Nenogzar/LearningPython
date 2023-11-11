"""""""""ЗАДАЧА 8  - стр. 130 """""""""
#  по въведено число от 1-7да се извежда съответното име от седмицата

week = {1: "Понеделник", 2: "Вторник", 3: "Сряда", 4: "Четвъртък", 5: "Петък", 6: "Събота", 7: "Неделя"}

day_number = int(input("Input day number: "))
day_name = week[day_number]

print(f"Ден {day_number} е {day_name}.") if day_number in week else print("Грешен номер на ден.")
