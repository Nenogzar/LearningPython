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
ab, bc, cd, da, ac, bd, slope_ab, slope_bc, slope_cd, slope_da = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
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


print(f"{small =}")
print(f"{larg = }")

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


print(f"{ab = :.2f}")
print(f"{bc = :.2f}")
print(f"{cd = :.2f}")
print(f"{da = :.2f}")
print(f"{ac = :.2f}")
print(f"{bd = :.2f}")



formula_perimeter = 0
formula_lice = 0
# square and rhombus
if ab == bc == cd == da:
    formula_perimeter = ab * 4
    if ac == bd:
        figure = "square"
        formula_lice = ab ** 2
    else:
        figure = "rhombus"
        formula_lice = ab * ac

# rectangle and parallelogram
elif ab == cd and bc == da:
    formula_perimeter = 2 * ab + 2 * bc
    if ac == bd:
        formula_lice = ab * bc
        figure = "rectangle"
    else:
        figure = "parallelogram"
        formula_lice = ab * ac

elif ac == bd:
    # isosceles trapezoid
    # slope of a segment - наклон на отсечка
    slope_ab = (new_coordinates[1][1] - new_coordinates[0][1]) \
               / (new_coordinates[1][0] - new_coordinates[0][0])

    # tochka na dopirane na wertikala
    # x = (y3 - y1 + m * x1 - m * x3) / m

    h_da1 = (
            new_coordinates[2][1]
            - new_coordinates[0][1]
            + slope_ab * new_coordinates[0][0]
            - slope_ab * new_coordinates[2][0])

    # Diagonal
    h = slope_ab * (h_da1- new_coordinates[2][0])
    visochina = abs(h) *10
    figure = "isosceles trapezoid"
    print(f"{h = }")
    print(f"{visochina = }")
    formula_perimeter = abs(ab) + abs(bc) + abs(cd) + abs(da)
    formula_lice = ((ab + cd) * visochina) / 2

else:
    formula_perimeter = abs(ab) + abs(bc) + abs(cd) + abs(da)



print(f"The figure is a {figure} whit perimeter: {formula_perimeter = :.2f} ")
print(f"The figure is a {figure} whit circumference: {formula_lice = :.2f} ")



