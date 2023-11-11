while True:
    # сортира където ключовете са запазени, а стойностите са сортирани възходящо
    my_dict = {"apple": 3, "banana": 1, "orange": 2}
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}


    print(sorted_dict)
    #print(sorted_dict1)

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
