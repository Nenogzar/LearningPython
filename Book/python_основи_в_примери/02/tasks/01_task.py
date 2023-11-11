"""""""""ЗАДАЧА 1  - стр. 129 """""""""
# num = input("Enter a number: ")
#
# if num.isdigit():
#     num = int(num)
#     num_len = len(str(num))
#     print(num_len)
# else:
#     print("Enter an integer, not text.")

""""""""" друго решение """""""""

num = input("Enter a number: ")

while not num.isdigit():
    print("Enter an integer, not text.")
    num = input("Enter a number: ")

num = int(num)
num_len = len(str(num))
print(num_len)
