# Речник за съпоставяне на буквите с числата
column_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
N = 8

# Входни данни с букви
horse_h = int(input())    # позиция на коня по вертикала
horse_x_letter = input()  # позиция на коня по хоризонтала (с буква)
other_h = int(input())    # позиция по вертикала на противникова фигура
other_x_letter = input()  # позиция по хоризонтала на противникова фигура

# Преобразуване на буквите в числови стойности за позицията на коня и противниковата фигура
horse_x = column_mapping.get(horse_x_letter, None)
other_x = column_mapping.get(other_x_letter, None)

if horse_h >= 1 and horse_h <= N and horse_x is not None:
    # Проверка на възможните ходове на коня
    possible_moves = []

    if horse_h + 1 <= N:
        if horse_x + 2 <= N:
            possible_moves.append((horse_h + 1, horse_x + 2))
        if horse_x - 2 >= 1:
            possible_moves.append((horse_h + 1, horse_x - 2))

    if horse_h - 1 >= 1:
        if horse_x + 2 <= N:
            possible_moves.append((horse_h - 1, horse_x + 2))
        if horse_x - 2 >= 1:
            possible_moves.append((horse_h - 1, horse_x - 2))

    if horse_h + 2 <= N:
        if horse_x + 1 <= N:
            possible_moves.append((horse_h + 2, horse_x + 1))
        if horse_x - 1 >= 1:
            possible_moves.append((horse_h + 2, horse_x - 1))

    if horse_h - 2 >= 1:
        if horse_x + 1 <= N:
            possible_moves.append((horse_h - 2, horse_x + 1))
        if horse_x - 1 >= 1:
            possible_moves.append((horse_h - 2, horse_x - 1))

    # Проверка дали конят може да удари противниковата фигура
    if (other_h, other_x) in possible_moves:
        other_x_letter = [key for key, value in column_mapping.items() if value == other_x][0]
        print(f'Конят може да удари противниковата фигура на позиция {other_h}{other_x_letter}.')
    else:
        print('Конят не може да удари противниковата фигура.')
else:
    print('Коня е  извън шахматната дъска')
