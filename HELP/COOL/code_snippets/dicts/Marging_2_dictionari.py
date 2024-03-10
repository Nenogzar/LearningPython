dict1 = {"apple": 3, "orange": 1}
dict2 = {"banana": 2, "pear": 4}

merge_dict = {**dict1, **dict2}
print(f"Обединени речници: {merge_dict}")

#Сортиране по ключове: тук ключовете са низове и сортира по азбучен ред
sorted_dict = dict(sorted(merge_dict.items()))
print(f"Сортирани речници: {sorted_dict}")

#Сортиране по индекс
sorted_by_value_dict = {k: v for k, v in sorted(merge_dict.items(), key=lambda item: item[1])}
print(f"Сортирани речници по индекс: {sorted_by_value_dict}")
