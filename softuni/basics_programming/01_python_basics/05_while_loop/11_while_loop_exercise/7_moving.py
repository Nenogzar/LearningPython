width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
space_left = 0

boxes_added = input()

while boxes_added != 'Done':

    total_space -= int(boxes_added)

    if total_space <= 0:
        print(f'No more free space! You need {abs(total_space)} Cubic meters more.')
        break
    boxes_added = input()

else:
    print(f'{total_space} Cubic meters left.')




# width = int(input())
# length = int(input())
# height = int(input())
#
# total_space = width * length * height
# space_left = 0
# while True:
#     boxes_added = input()
#     if boxes_added == "Done":
#         space_left += - total_space
#         print(f"{abs(space_left)} Cubic meters left.")
#         break
#     space_left += + int(boxes_added)
#     if total_space < space_left:
#         total_space = space_left - total_space
#         print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
#         break
