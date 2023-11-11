# проверка дали е едноцифрено число ->  0<=n<10
def get_single_digit(number):
    if len(number) == 1 and number.isdigit():
        return True
    else:
        return False


while True:

    input_number = input("enter a number: ")
    if get_single_digit(input_number):
        print("Valid single digit")
    else:
        print("Not valid single digit. Tray again.")
        continue
    print("Singe digit you enter is :", input_number)


    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
