""" 1 """
# float_number = float(input())
# if float_number == 0:
#     print("zero")

# if float_number > 0:
#     if float_number < 1:
#         print('small positive')
#     elif float_number > 1000000:
#         print('larg positive')
#     else:
#         print('positive')

# if float_number < 0:
#     if abs(float_number) < 1:
#         print('small negative')
#     elif abs(float_number) > 1000000:
#         print('larg negative')
#     else:
#         print('negative')

""" 2 """
float_number = float(input())

if float_number == 0:
    print('zero')
elif 0 < float_number < 1:
    print('small positive')
elif 1 <= float_number <= 1000000:
    print('positive')
elif -1 >= float_number >= -1000000:
    print('negative')
elif float_number < 0:
    print('small negative')
else:
    print('large negative')