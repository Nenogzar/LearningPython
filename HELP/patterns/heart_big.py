""" 1 """
# print('\n'.join(
#     ([''.join
#       ([("promenliva"[(x-y)%8]
#         if((x*0.05)**2+(y*0.1)**2-1)
#          **3-(x*0.05)**2*(y*0.1)
#          **3<=0 else ' ')
#         for x in range(-30,30)])
#             for y in range(15,-15,-1)])))

""" 2 """
# promenliva = input("Input name: ")
# name_length = len(promenliva)
#
# print('\n'.join(
#     ([''.join
#       ([promenliva[(x-y) % name_length]
#         if((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0 else ' '
#         for x in range(-30, 30)])
#             for y in range(15, -15, -1)])))

""" 3 """


def generate_pattern(input_name):
    name_length = len(input_name)
    pattern = '\n'.join([''.join([input_name[(x - y) % name_length]
                                  if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
                y * 0.1) ** 3 <= 0 else ' '
                                  for x in range(-30, 30)])
                         for y in range(15, -15, -1)])
    return pattern


input_name = input("Input name: ")
result = generate_pattern(input_name)
print(result)
