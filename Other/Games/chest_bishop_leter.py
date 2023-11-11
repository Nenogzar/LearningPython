def is_valid_coordinate(x, y, n):
    # Проверка дали координатите са валидни за даден размер на дъската (от 1 до n)
    return 1 <= x <= n and 1 <= y <= n

def convert_letter_to_number(letter):
    # Преобразуване на буквени обозначения за колоните в числови стойности
    letter = letter.lower()  # Не зависи от главни/малки букви
    if letter == 'a':
        return 1
    elif letter == 'b':
        return 2
    elif letter == 'c':
        return 3
    elif letter == 'd':
        return 4
    elif letter == 'e':
        return 5
    elif letter == 'f':
        return 6
    elif letter == 'g':
        return 7
    elif letter == 'h':
        return 8
    else:
        return None

def convert_number_to_letter(number):
    # Преобразуване на числови стойности за колоните в буквени обозначения
    if 1 <= number <= 8:
        return chr(ord('a') + number - 1)
    else:
        return None

def can_bishop_capture(bishop_x, bishop_y, target_x, target_y, n):
    if not (is_valid_coordinate(bishop_x, bishop_y, n) and is_valid_coordinate(target_x, target_y, n)):
        print("Координатите са извън дъската.")
        return False

    # Проверка дали белият офицер и фигурата, която искате да проверите, са на едно и също цветово поле
    if (bishop_x + bishop_y) % 2 != (target_x + target_y) % 2:
        print("Белият офицер и фигурата не са на едно и също цветово поле.")
        return False

    # Преобразуване на числовите стойности на фигурата в буквени обозначения
    target_col = convert_number_to_letter(target_x)
    target_row = str(target_y)

    # Проверка дали офицерът може да вземе фигурата, като проверим дали разликата
    # в абсолютните стойности на координатите по редове и колони е еднаква
    if abs(bishop_x - target_x) == abs(bishop_y - target_y):
        print(f"Белият офицер може да вземе фигурата с координати - {target_col}{target_row}.")
        return True
    else:
        print(f"Белият офицер не може да вземе фигурата с координати - {target_col}{target_row}.")
        return False

def main():
    n = 8  # Размер на дъската

    # Въведете координатите на белия офицер
    bishop_col = input("Въведете колона на белия офицер (a-h): ")
    bishop_row = int(input("Въведете ред на белия офицер (1-8): "))
    bishop_x = convert_letter_to_number(bishop_col)

    # Въведете координатите на фигурата, която искате да проверите
    target_col = input("Въведете колона на фигурата (a-h): ")
    target_row = int(input("Въведете ред на фигурата (1-8): "))
    target_x = convert_letter_to_number(target_col)

    can_bishop_capture(bishop_x, bishop_row, target_x, target_row, n)

if __name__ == "__main__":
    main()
