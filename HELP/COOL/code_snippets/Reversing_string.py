while True:
    # реверсия на текст
    string = input("Въведи текст")
    reversed_str = string[::-1]
    print(reversed_str)

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
