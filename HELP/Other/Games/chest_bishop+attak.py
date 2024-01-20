def is_valid_coordinate(x, y, n):
    # Проверка дали координатите са валидни за даден размер на дъската (от 1 до n)
    return 1 <= x <= n and 1 <= y <= n

def can_bishop_capture(bishop_x, bishop_y, target_x, target_y, n):
    if not (is_valid_coordinate(bishop_x, bishop_y, n) and is_valid_coordinate(target_x, target_y, n)):
        print("Координатите са извън дъската.")
        return False

    # Проверка дали белият офицер и фигурата, която искате да проверите, са на едно и също цветово поле
    if (bishop_x + bishop_y) % 2 != (target_x + target_y) % 2:
        print("Офицера и фигурата не са на едно и също цветово поле.")
        return False

    # Проверка дали офицерът може да вземе фигурата, като проверим дали разликата
    # в абсолютните стойности на координатите по редове и колони е еднаква
    if abs(bishop_x - target_x) == abs(bishop_y - target_y):
        print("Офицера може да вземе фигурата.")
        return True
    else:
        print("Офицера не може да вземе фигурата.")
        return False

def main():
    n = 8  # Размер на дъската

    # Въведете координатите на белия офицер
    bishop_x = int(input("Въведете ред на офицера (1-8): "))
    bishop_y = int(input("Въведете колона на офицера (1-8): "))

    # Въведете координатите на фигурата, която искате да проверите
    target_x = int(input("Въведете ред на фигурата (1-8): "))
    target_y = int(input("Въведете колона на фигурата (1-8): "))

    can_bishop_capture(bishop_x, bishop_y, target_x, target_y, n)

if __name__ == "__main__":
    main()
