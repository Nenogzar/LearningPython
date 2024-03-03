def is_positive(n: int) -> bool:
    return n >= 0

def is_armstrong(n: int) -> bool:
    if not is_positive(n):
        return False

    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n

def main():
    while True:
        try:
            num = int(input("Enter a number: "))

            if is_armstrong(num):
                #num_str = str(num)
                #num_digits = len(num_str)
                #formula = " + ".join([f"{digit}^{num_digits}" for digit in num_str])
                # с следващия код се примахват променливите за Str  и len  и се съкращава кода
                formula = " + ".join([f"{digit}^{len(str(num))}" for digit in str(num)])

                print(f"{num} is an Armstrong number. It follows the formula: {formula}")
            else:
                print(f"{num} is not an Armstrong number.")

            repeat = input("Do you want to repeat? (Y/N): ").strip().lower()
            if repeat != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()