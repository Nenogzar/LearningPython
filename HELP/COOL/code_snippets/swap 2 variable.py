
while True:
    def method(a, b):
        print("Начални стойности:")
        print(f"a ={a} ({bin(a)[2:]} в двоична система)")
        print(f"b = {b} ({bin(b)[2:]} в двоична система)")

        a = a ^ b
        print("\nСлед a = a ^ b:")
        print(f"a = {a} ({bin(a)[2:]} в двоична система)")
        print(f"b = {b} ({bin(b)[2:]} в двоична система)")

        b = a ^ b
        print("\nСлед b = a ^ b:")
        print(f"a = {a} ({bin(a)[2:]} в двоична система)")
        print(f"b = {b} ({bin(b)[2:]} в двоична система)")

        a = a ^ b
        print("\nСлед a = a ^ b:")
        print(f"a = {a} ({bin(a)[2:]} в двоична система)")
        print(f"b = {b} ({bin(b)[2:]} в двоична система)")

        return a, b

    input_a = int(input("Въведете стойност за a: "))
    input_b = int(input("Въведете стойност за b: "))

    result = method(input_a, input_b)
    print("\nНовите стойности след размяната:")
    print(f"a = {result[0]} ({bin(result[0])[2:]} в двоична система)")
    print(f"b = {result[1]} ({bin(result[1])[2:]} в двоична система)")

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("10x!")
        break
