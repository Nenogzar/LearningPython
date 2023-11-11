"""""""""ЗАДАЧА 5  - стр. 130 """""""""

list1 = list(map(int, input("Въведете списък от числа, разделени със запетайка: ").split(',')))
number = int(input("Въведете горна граница: "))
sum_num = 0

for num in range(1, number+1):
    sum_num += num
#print("Сумата на границата е: ", sum_num)
sum_list = sum(list1)
#print("Сумата от аргументите на списъка е: ", sum_list)
result = sum_num - sum_list
print("РЕЗУЛТАТ: ", result)
