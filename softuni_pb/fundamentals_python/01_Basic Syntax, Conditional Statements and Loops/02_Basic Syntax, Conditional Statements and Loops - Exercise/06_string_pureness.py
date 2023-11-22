num_str = int(input())

for string in range(num_str):
    pure_str = input()
    if "," in pure_str or \
        "." in pure_str or \
        "_" in pure_str:
        print(f"{pure_str} is not pure!")
    else:
        print(f"{pure_str} is pure.")