# Изходен списък:
A = [1, 3, [10, 20], "Python", [40, 50]]
# Създаване на повърхностно копие на списъка:
B = A[:]
C = A.copy()
print("Изходни стойности:")
print("A:", A)
print("B:", B)
print("C:", C)
# Внасяне на изменения в изходния списък:
A[0] = [100, 200]
A[2][1] = 300
A[3] = "Java"
A[4] = 90
C[4][1] = "C++"
print("След измененията:")
print("A:", A)
print("B:", B)
print("C:", C)
