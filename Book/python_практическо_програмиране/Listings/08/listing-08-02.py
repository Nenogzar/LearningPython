cars = []

print("*" * 10, " Garage v.0.0.1 ", "*" * 10)

responce = 1
while responce:
    print("""Изберете действие:
           1 - Add vehicle
           2 - Remove the vehicle
           3 - Display the list of cars
           4 - Find a car
           5 - Sort the garage
           0 - Exit""")
    responce = int(input(">> "))
    if responce == 1:
        car = input("Add vehicle: ")
        cars.append(car)
    elif responce == 2:
        car = input("Remove the vehicle: ")
        cars.remove(car)
    elif responce == 3:
        print(cars)
    elif responce == 4:
        car = input("Find a car: ")
        if car in cars:
            print("Such a car is in the garage!")
        else:
            print("There's no such car in the garage!")
    elif responce == 5:
            cars.sort()
            print("Sorted!")
    else:
            print("See you soon!")
