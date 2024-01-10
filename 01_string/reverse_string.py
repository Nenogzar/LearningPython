while True:

    def reverse_string(string):
        return string[::-1]


    a = input("enter text: ")
    print(reverse_string(a))

    repeat = input("Would you like to repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("Thanks!")
        break
