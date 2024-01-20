""" List Comprehension """
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
newlist3 = []

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.############
[newlist.append(x) for x in fruits if "a" in x]
"""['apple', 'banana', 'mango']"""
######################################   -- OR -- ######################################################################
newlist1 = [x for x in fruits if "a" in x]
"""['apple', 'banana', 'mango']"""
#Example: Only accept items that are not "apple"########################################################################
newlist2 = [x for x in fruits if x != "apple"]
"""['banana', 'cherry', 'kiwi', 'mango']"""
#-With no if statement-#################################################################################################
newlist3 = [x for x in fruits] """OR"""  [newlist3.append(x) for x in fruits]
"""["apple", "banana", "cherry", "kiwi", "mango"]"""
########################################-range()-#######################################################################
# Example: You can use the range() function to create an iterable:
newlist4 = [x for x in range(10)]
"""[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

number = [int(input(f"{n} число: ")) for n in range(1, int(input("Създаване на списък с дължина: "))+1)]
print(number)

#####################################-lower-############################################################################
# Example: Accept only numbers lower than 5:
newlist5 = [x for x in range(10) if x < 5]
# [0, 1, 2, 3, 4]
######################################-UPPER-###########################################################################
# Example: Set the values in the new list to UPPER case:
newlist6 = [x.upper() for x in fruits]
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
##Example: Set all values in the new list to 'hello':###################################################################
newlist7 = ['hello' for x in fruits]
# ['hello', 'hello', 'hello', 'hello', 'hello']
#Example: Return "orange" instead of "banana":##########################################################################
newlist8 = [x if x != "banana" else "orange" for x in fruits]
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']
########################################################################################################################
s = [int(x) for x in input().split()]

#########################- средана част на списък от четни числа -######################################################
up = int(input("горна граница на листа: "))
test_list = list(x for x in (list(x for x in range(1, up))) if x in range(0, up, 2))
print(test_list)
print(test_list[up // 7:(up // 3) + 1])

########################################################################################################################
