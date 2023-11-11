while True:

    num1 = int(input("кое е числото? "))
    import random
    num_random = random.randint(1, 100)
    print(num_random)



    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
