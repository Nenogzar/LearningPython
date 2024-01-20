import random

num_ran = random.randint(1, 100)
print(num_ran)

guess_count = 0  # Променлива за брояч на опитите

while True:
    guess_count += 1  # Увеличаваме брояча с 1 при всяко ново опитване
    num1 = int(input("кое е числото? "))

    if num1 < num_ran:
        print("По-нагоре ")
        continue
    elif num1 > num_ran:
        print("По-надолу")
        continue
    else:
        print(f"Браво позна числото след {guess_count} опита!")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
