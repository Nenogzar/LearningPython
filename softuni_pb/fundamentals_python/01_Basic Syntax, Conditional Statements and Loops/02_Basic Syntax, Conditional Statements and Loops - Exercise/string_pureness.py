num_str = int(input())

for string in range(num_str):
    pure_str = input()
    if "," in pure_str or \
        "." in pure_str or \
        "_" in pure_str:
        print(f"{pure_str} is not pure!")
    else:
        print(f"{pure_str} is pure.")


""" 2 """
how_many_strings = int(input())

skip_parameters = [",", ".", "_"]

for _ in range(how_many_strings):
    string_ = input()
    for element in skip_parameters:
        if element in string_:
            print(f"{string_} is not pure!")
            break
    else:
        print(f"{string_} is pure.")