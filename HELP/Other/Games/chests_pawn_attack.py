def pawn_attack(x, y, p, q):
    """
    Определя дали пешката с координати x, y от шахматната дъска с размери n - реда и n - колони n >= 8 се бие от фигура разположена в поле с координати p, q, ако фигурата е ПЕШКА.

    Args:
        x: Координата x на пешката.
        y: Координата y на пешката.
        p: Координата x на фигурата.
        q: Координата y на фигурата.

    Returns:
        True, ако пешката се бие, False, ако не се бие.
    """

    # Проверки за валидност на координатите
    if x < 0 or x >= 8:
        raise ValueError("Невалидна координата x.")
    if y < 0 or y >= 8:
        raise ValueError("Невалидна координата y.")
    if p < 0 or p >= 8:
        raise ValueError("Невалидна координата p.")
    if q < 0 or q >= 8:
        raise ValueError("Невалидна координата q.")

    # Проверка за нападение на пешката
    dx = abs(x - p)
    dy = abs(y - q)

    # пешката може да бие по диагоналите (1, 1), (1, -1), (-1, 1), (-1, -1)
    return (dx == dy) and (dx == 1 or dx == 2)


if __name__ == "__main__":
    x = int(input("Въведете x: "))
    y = int(input("Въведете y: "))
    p = int(input("Въведете p: "))
    q = int(input("Въведете q: "))

    try:
        result = knight_attack(x, y, p, q)
        if result:
            print("пешката бие фигурата.")
        else:
            print("пешката не бие фигурата.")
    except ValueError as e:
        print(e)
