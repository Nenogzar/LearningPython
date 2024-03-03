# проверява дали числото е в диапазона 1 - 9
while True:

    def get_single_digit(number):  # дефиниране на функция за проверка
        if len(number) == 1 and number.isdigit():
            return True
        else:
            return False

    while True:
        input_number = input("Enter a number: ")
        if get_single_digit(input_number):  # използваме функцията за да направим проверка на валидно число
            print("Valid single digit")
            break
        else:
            print("Not a valid single digit. Try again.")
    print("Single digit you enter is: ", input_number)


    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
