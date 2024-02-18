# Example:
# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even).
# Finally, print the result.

numbers = [int(input(f"-{i+1}- ")) for i in range(int(input("range: ")))]
command = input("odd / even / positive / negative :")

# print([x for x in numbers if any([command == "odd" and x % 2 != 0,
#                                   command == "even" and x % 2 ==0,
#                                   command == "positive" and x >= 0,
#                                   command == "negative" and x < 0])])


result = [x for x in numbers if any([command == "odd" and x % 2 != 0,
                                     command == "even" and x % 2 == 0,
                                     command == "positive" and x >= 0,
                                     command == "negative" and x < 0])]

print(f"{command} in list {numbers} is {result}")
print(f"in list {numbers} have a {len(result)} {command} elements: {result}")
