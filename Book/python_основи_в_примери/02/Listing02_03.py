# Въвеждане на число:
number=int(input("Въведете число: "))
# Съобщение за първия делител на числото:
print("Дели се на",1)
# Начална стойност за делителя:
k=1
# Търсене на делителите на числото:
while k < number // 2:
    # Стойността на делителя се увеличава с единица:
    k = k + 1
    # Ако k не е делител на числото:
    if number % k != 0:
        # Край на текущата итерация:
        continue
    # Съобщение за делителя на числото:
    print("Дели се на",k)
# Съобщение за последния делител на числото:
print("Дели се на",number)
