import random

num_ran = random.randint(1, 100)
print(num_ran)

guess_count = 0

while True:
    guess_count += 1
    num1 = int(input("what is the number? "))

    if num1 < num_ran:
        print("Higher ")
        continue
    elif num1 > num_ran:
        print("Below")
        continue
    else:
        print(f"Well done guess the number after {guess_count} tries!")

    repeat = input("Do you want to replay the game? (Y/N)? ")
    if repeat.upper() == "N":
        print("thank you!")
        break
