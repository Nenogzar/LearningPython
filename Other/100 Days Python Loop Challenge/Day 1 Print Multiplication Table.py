while True:
    def print_multiplication_table(n):
        for i in range(1, 10):
            for j in range(1, n+1):
                print(i * j, end='\t' )
            print()

    mul = int(input("Enter the number you want the table for: "))
    print_multiplication_table(mul)

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
