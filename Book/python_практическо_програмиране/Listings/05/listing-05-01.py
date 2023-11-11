import random

print("*" * 10, "Guess the number", "*" * 10)

print("The computer will guess the number from 1 to 10. Try to guess the number. To exit enter 0")

answer = 1;
score = 0;
i = 0

while answer:
    
    rand = random.randint(1, 10)
    answer = int(input("Enter the number: "))

    if answer == 0: 
      break
    if answer == rand:
        score = score +1
        print("Correctly!")
    else:
        print("Sorry :(")
    i = i + 1    

print("Total score ", score, " from ", i)
print("See you next time!")
