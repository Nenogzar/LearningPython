# Функцията връща общия брой на последователните двойки "1" - total.

def count_consective_ones(lst):
    count = 0
    total = 0
    for num in lst:
        if num == num1:
            count += 1
            if count == 2:
                total += 1
        else:
            count = 0
    return total

while True:

    elements = input("Enter the elements of the list (space-separated): ").split()
    my_list = [int(elem) for elem in elements]
    num1 = int(input("Последователна двойка от koe число ще търсим? "))
    print(f"my list is: {my_list}")
    occurrences = count_consective_ones(my_list)
    print(f"Occurrences of two consecutive ones: {occurrences}")


    repeat = input("Do you want to repeat? Y/N: ")
    if repeat.upper() == "N":
        print("Thank you!")
        break
