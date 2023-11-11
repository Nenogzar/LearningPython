    #премахване на item от листа my_list

while True:
                                    # дефиниране на променлива която присвоява текст
    input_string = input("Въведете части на списък, разделени със запетайка: ")
    input_parts = input_string.split(',')
    my_list = input_parts
    item=input("Item ?")

    me_list = [x for x in my_list if x.strip() != item]
                                    # x.strip() != item: Това е условието, което проверява дали текущия елемент x,
                                    # след премахване на възможни интервали около него, не е равен на зададения item.
    print(me_list)

    parts = [int(part.strip()) for part in my_list]
                                    # for part in my_list - извършва обхождане на всеки елемент от списъка me_list
                                        # strip() методът се използва, за да премахне възможни интервали или празни
                                            # символи от началото и края на текущия низ.
                                    # [int(part.strip()) for part in me_list]: Списъковият израз създава нов списък,
                                        # като преминава през всеки елемент part от me_list,
                                            # преобразува го към цяло число и добавя резултатите в новия списък.

    print(parts)

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("10x!")
        break