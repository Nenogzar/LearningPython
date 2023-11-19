
scale_x = 0.04
scale_y = 0.1
for y in range(20, -20, -1):
    line = ''
    for x in range(-30, 30):
        if (((x * scale_x) ** 2 + (y * scale_y) ** 2 - 1) ** 3 - (x * scale_x) ** 2 * (y * scale_y) ** 3) <= 0:
            line += '*'
        else:
            line += ' '
    print(line)