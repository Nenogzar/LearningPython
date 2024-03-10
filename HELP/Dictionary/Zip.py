num_list = input("Имена на речника ")
list1 = []
list2 = []
other_list =[]
for num in range(len(num_list)):
    list_number = num + 1
    list1.append(list_number)
    arguments_list2 = input("Въведи елементите от списъка")
    list2.append(arguments_list2)

    # dictionary
    my_dict = dict(zip(list1, list2))

    dict_new = dict(zip(range(len(num_list)), list2))

    # lists
    nested_list = list(zip(range(len(num_list)), list2))

    # for item in zip(range(num_list), list2, strict=False):
    #     print(item)


print("nested_list ->", nested_list)
print("my_dict ->", my_dict)
print("dict_new ->", dict_new)
print("other_list->", other_list)
