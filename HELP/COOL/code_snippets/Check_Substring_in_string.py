while True:
    # Търсене на съвпадение в текст
    string = input("Въведи текст")
    substring = "World"
    if substring in string:
        print("Sunstring i found")
    else:
        print("Substring not found")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
