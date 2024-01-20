class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        raise ValueError("Invalid operation. You can only add two Point objects.")

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        raise ValueError("Invalid operation. You can only subtract two Point objects.")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Point(self.x * scalar, self.y * scalar, self.z * scalar)
        raise ValueError("Invalid operation. You can only multiply a Point by a number.")

    def __rmul__(self, scalar):
        # This allows multiplication in the order of scalar * Point
        return self.__mul__(scalar)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

# Example usage:
p1 = Point(1, 2, 3)
x, y, z = p1
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
