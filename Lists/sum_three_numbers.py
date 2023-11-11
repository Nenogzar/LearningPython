a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

x1 = a + b
x2 = b + c
x3 = c + a

res1 = c + x1
res2 = a + x2
res3 = b + x3

print(res1, res2, res3)

""""List"""

num = list()                # дефиниране на списък
total = 0
for number in range(3):     # определяне сължината на списъка
    inp = input('Enter three numbers: ')    # въвеждане на елементите от списъка
    num.append(int(inp))       # добавяне на аргументите в списъка като ги преобразува в int
    # пресмятане на списъка като събираме съседните аргументи и последния с първия
    res = [num[i] + num[(i + 1) % len(num)] for i in range(len(num))]   # % len(num) прави кръгово - пресмятане последен с първи
    total = [num[i -1] + res[i] for i in range(len(res))]   # сумниране на аргументите от num и res като първия се сумира с последния

#print(res)
print(total)

""""NEXT"""

elements = input("Enter the elements of the list (space-separated): ").split()  # дефиниране и съставяне на слисък
my_list = [int(a) for a in elements]    # преобразуване на аргументите от списъка от str в int
m_sum = [my_list[i] + my_list[ (i + 1) % len(my_list)] for i in range(len(my_list))]    # дефиниране на нов списък със аргументи сумата на аргументие от my_list сумирани по съседство и последния с първия
total_list = [my_list[i-1] + m_sum[i] for i in range(len(my_list))] # съставяне на списък с аргументи от двата спуисъка като се сумират по диагонал - my_list[-1] + m_sum[0] до края

print(total_list)

"""""next"""

chisla = input("Enter the number of the list whit space-separated: ").split()
chisla_list_int = [int(i) for i in chisla]
sum_arguments = sum(chisla_list_int)
me_list_chisla = [sum_arguments] * len(chisla_list_int)

print(me_list_chisla)
