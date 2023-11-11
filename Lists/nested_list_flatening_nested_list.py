while True:
    input_string = input("Въведете числа, разделени със запетайка: ")
    input_numbers = input_string.split(',')


    # обхожда списъка и разделя на двойки вложени списъци
    pairs = [input_numbers[i:i + 2] for i in range(0, len(input_numbers) - 1, 2)]

    # еко е нечетен брой добавям последния елемент като отделен вложен списък в pairs
    if len(input_numbers) % 2 == 1:
        pairs.append([input_numbers[-1]])

    pairs = [[int(num) for num in pair] for pair in pairs]
    print("Вложени списъци:", pairs)
                    #извлича всички елементи от вложените списъци в pairs
                    # и ги обединява в един плосък (едномерен) списък.
    flat_list = [x for sublist in pairs for x in sublist]
    print("Обединен списък:", flat_list)

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
