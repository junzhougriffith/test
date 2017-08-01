##////////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Implement a Vector2D class which allows the following statements to execute //
##///////////////////////////////////////////////////////////////////////////////


class Vector2D:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return str(self.x)  + str(self.y)

    def __add__(self, other):
        f = Vector2D(self.x + other.x, self.y + other.y)
        return f

    def __sub__(self, other):
        f = Vector2D(self.x - other.x, self.y - other.y)
        return f

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
v1 = Vector2D(int(input()), int(input()))
v2 = Vector2D(int(input()), int(input()))
v3 = Vector2D(v1.x, v1.y)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)  # Dot product = x1 * x2 + y1 * y2
print(v3 == v1)
