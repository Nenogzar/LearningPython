def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


elements = input("Enter the elements of the list (space-separated): ").split()
my_list = [int(a) for a in elements]
print((my_list))

target = int(input("Enter the element to search for: "))
index = linear_search(my_list, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not in the list")


