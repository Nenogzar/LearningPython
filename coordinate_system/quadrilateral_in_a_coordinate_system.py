# """ calculation of a quadrilateral in a coordinate system """
# coordinate_a = list(map(int, input("A: ").split()))
# coordinate_b = list(map(int, input("B: ").split()))
# coordinate_c = list(map(int, input("C: ").split()))
# coordinate_d = list(map(int, input("D: ").split()))
#
# # Поправки във формулата
# formula = 0.5 * (
#     (coordinate_a[0] * coordinate_b[1])
#     + (coordinate_b[0] * coordinate_c[1])
#     + (coordinate_c[0] * coordinate_d[1])
#     + (coordinate_d[0] * coordinate_a[1])
#     - (coordinate_b[0] * coordinate_a[1])
#     - (coordinate_c[0] * coordinate_b[1])
#     - (coordinate_d[0] * coordinate_c[1])
#     - (coordinate_a[0] * coordinate_d[1])
# )
#
# print("Лицето на четириъгълника е:", abs(formula))

""" calculation of a quadrilateral in a coordinate system - with a check for correctly arranged coordinate points """
import math
ab, bc, cd, da, ac, bd, = 0, 0, 0, 0, 0, 0,
figure = ''
coordinate_a = list(map(int, input("Enters two integers with a space between them: ").split()))
coordinate_b = list(map(int, input("Enters two integers with a space between them: ").split()))
coordinate_c = list(map(int, input("Enters two integers with a space between them: ").split()))
coordinate_d = list(map(int, input("Enters two integers with a space between them: ").split()))

coordinates = [coordinate_a, coordinate_b, coordinate_c, coordinate_d]

small = coordinates[0]
larg = coordinates[0]

for coordinate in coordinates[1:]:
    if sum(coordinate) < sum(small):
        small = coordinate

    if sum(coordinate) > sum(larg):
        larg = coordinate


print("the smallest coordinate", small)
print("the largest coordinate", larg)

new_coordinates = coordinates.copy()
new_coordinates.remove(small)
new_coordinates.remove(larg)
new_coordinates.insert(0, small)
new_coordinates.insert(2, larg)


print("the ordered list of coordinates is", new_coordinates)


formula = 0.5 * ( + new_coordinates[0][0] * new_coordinates[1][1]
                  + new_coordinates[1][0] * new_coordinates[2][1]
                  + new_coordinates[2][0] * new_coordinates[3][1]
                  + new_coordinates[3][0] * new_coordinates[0][1]
                  - new_coordinates[1][0] * new_coordinates[0][1]
                  - new_coordinates[2][0] * new_coordinates[1][1]
                  - new_coordinates[3][0] * new_coordinates[2][1]
                  - new_coordinates[0][0] * new_coordinates[3][1]
                  )

print("The perimeter of the quadrilateral is:", abs(formula))

ab = ((new_coordinates[0][0] - new_coordinates[1][0])**2 + (new_coordinates[0][1] - new_coordinates[1][1])**2)**0.5
bc = ((new_coordinates[1][0] - new_coordinates[2][0])**2 + (new_coordinates[1][1] - new_coordinates[2][1])**2)**0.5
cd = ((new_coordinates[2][0] - new_coordinates[3][0])**2 + (new_coordinates[2][1] - new_coordinates[3][1])**2)**0.5
da = ((new_coordinates[3][0] - new_coordinates[0][0])**2 + (new_coordinates[3][1] - new_coordinates[0][1])**2)**0.5
# diagonals
ac = ((new_coordinates[0][0] - new_coordinates[2][0])**2 + (new_coordinates[0][1] - new_coordinates[2][1])**2)**0.5
bd = ((new_coordinates[1][0] - new_coordinates[3][0])**2 + (new_coordinates[1][1] - new_coordinates[3][1])**2)**0.5


# Отпечатайте дължините на отсечките
print(f"AB = {ab:.2f}")
print(f"BC = {bc:.2f}")
print(f"CD = {cd:.2f}")
print(f"DA = {da:.2f}")
print(f"Диагонала AC = {da:.2f}")
print(f"Диагонала BD  = {da:.2f}")

formula_by_type = 0

if ab == bc == cd == da:
    if ac == bd:
        figure = "square"
        formula_by_type = ab ** 2
    else:
        figure = "rhombus"
        formula_by_type = (ac * bd) /2

if ab == cd and bc == da:
    formula_by_type = 2 * ab + 2 * bc
    if ac == bd:
        figure = "rectangle"
    else:
        figure = "parallelogram"
        formula_by_type = 2 * ab + 2 * bc





print(f"The figure is a {figure} whit perimeter: {formula_by_type} ")





