N = 8               #   шахматна дъска n реда на  n колони
horse_h = int(input())    #   позиция на коня по вертикала
horse_x = int(input())    #   позиция на коня по хоризонтала
other_h = int(input())    #   позиция по вертикала на противникова фигура
other_x = int(input())    #   позиция по хоризонтала на противникова фигура

if horse_h<= N and horse_x <= N:
    if (horse_h+1 <= N) and (horse_x+2 <= N):
        print('1: ', (horse_h+1), ', ', (horse_x+2))
    if (horse_h+1 <= N) and (horse_x-2 >= 1):
        print('2: ',(horse_h+1), ', ', (horse_x-2))
    if (horse_h-1 >= 1) and (horse_x+2 <= N):
        print('3: ',(horse_h-1), ', ', (horse_x+2))
    if (horse_h-1 >= 1) and (horse_x-2 >= 1):
        print('4: ',(horse_h-1), ', ', (horse_x-2))
    if (horse_h+2 <= N) and (horse_x+1 <= N):
        print('5: ',(horse_h+2), ', ', (horse_x+1))
    if (horse_h+2 <= N) and (horse_x-1 >= 1):
        print('6: ',(horse_h+2), ', ', (horse_x-1))
    if (horse_h-2 >= 1) and (horse_x+1 <= N):
        print('7: ',(horse_h-2), ', ', (horse_x+1))
    if (horse_h-2 <= N) and (horse_x-1 >= 1):
        print('8: ',(horse_h-2), ', ', (horse_x-1))
else:
    print('Фигура извън шахматната дъска')

# Речник за съпоставяне на числовите стойности с буквите
column_mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

# Проверка дали конят може да удари противниковата фигура
if (other_h, other_x) in [
    (horse_h+1, horse_x+2),
    (horse_h+1, horse_x-2),
    (horse_h-1, horse_x+2),
    (horse_h-1, horse_x-2),
    (horse_h+2, horse_x+1),
    (horse_h+2, horse_x-1),
    (horse_h-2, horse_x+1),
    (horse_h-2, horse_x-1)
]:
    # Преобразуване на числовите стойности в букви за позицията на противниковата фигура
    other_x_letter = column_mapping.get(other_x, 'unknown')
    print(f'Конят може да удари противниковата фигура на позиция {other_x_letter}{other_h}.')
else:
    print('Конят не може да удари противниковата фигура.')
