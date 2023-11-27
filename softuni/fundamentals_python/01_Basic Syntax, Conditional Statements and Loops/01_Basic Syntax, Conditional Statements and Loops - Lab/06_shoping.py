budget = int(input())
total = 0
while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break
    current_price = float(command)
    budget -= current_price
    if budget <= 0:
        print("You went in overdraft!")
        break


