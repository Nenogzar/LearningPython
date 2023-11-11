import re
def mult(m):
	x = int(m.group(0))
	x *= 2
	return "{0}".format(x)

p = re.compile(r"[0-9]+")
# умножававме всички числа на 2
print(p.sub(mult, "2, 3, 4, 5, 6, 7, 8, 9, 10"))
# умножававме първите три числа
print(p.sub(mult, "2, 3, 4, 5, 6, 7, 8, 9, 10", 5))
