while True:
    number = float(input())

    if number < 0:
        print("Negative number!")
        break

    result = number * 2
    print(f"Result: {result:.2f}")


# number = float(input())
# while number >= 0:
#     print(f"Result: {number * 2:.2f}")
#     number = float(input())
#
# print("Negative number!")
