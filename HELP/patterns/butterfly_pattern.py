# Butterfly pattern
r = int(input("Enter the size of the butterfly: "))
# Open triangle
for i in range(1, r + 1):
    print("*" * i, end="")
    print(" " * (r - i) * 2, end="")
    print("+" * i)
# Lower triangle
for i in range(r - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (r - i) * 2, end="")
    print("*" * i)
