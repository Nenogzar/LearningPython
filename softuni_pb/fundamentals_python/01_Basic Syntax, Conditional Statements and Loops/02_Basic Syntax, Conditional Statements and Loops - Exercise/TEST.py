
coordinate_a = list(map(int, input("Въведи две цели числа с интервал по между им: ").split()))
coordinate_b = list(map(int, input("Въведи две цели числа с интервал по между им: ").split()))
coordinate_c = list(map(int, input("Въведи две цели числа с интервал по между им: ").split()))
coordinate_d = list(map(int, input("Въведи две цели числа с интервал по между им: ").split()))

coordinates = [coordinate_a, coordinate_b, coordinate_c, coordinate_d]

small = coordinates[0]
larg = coordinates[0]

for coordinate in coordinates[1:]:
    if sum(coordinate) < sum(small):
        small = coordinate

    if sum(coordinate) > sum(larg):
        larg = coordinate


print("май - малкия", small)
print("най - големия", larg)

new_coordinates = coordinates.copy()
new_coordinates.remove(small)
new_coordinates.remove(larg)
new_coordinates.insert(0, small)
new_coordinates.insert(2, larg)


print("новият списък с координати е", new_coordinates)


formula = 0.5 * ( + new_coordinates[0][0] * new_coordinates[1][1]
                  + new_coordinates[1][0] * new_coordinates[2][1]
                  + new_coordinates[2][0] * new_coordinates[3][1]
                  + new_coordinates[3][0] * new_coordinates[0][1]
                  - new_coordinates[1][0] * new_coordinates[0][1]
                  - new_coordinates[2][0] * new_coordinates[1][1]
                  - new_coordinates[3][0] * new_coordinates[2][1]
                  - new_coordinates[0][0] * new_coordinates[3][1]
                  )

print("Лицето на четириъгълника е:", abs(formula))
