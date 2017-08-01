##////////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Implement a Vector3D class which allows the following statements to execute //
##///////////////////////////////////////////////////////////////////////////////


class Vector3D:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.z)

    def __add__(self, other):
        f = Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return f

    def __sub__(self, other):
        f = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return f

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        f = Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        return f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
v1 = Vector3D(int(input()), int(input()), int(input()))
v2 = Vector3D(int(input()), int(input()), int(input()))
v3 = Vector3D(v1.x, v1.y, v1.z)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)  # Dot product = x1 * x2 + y1 * y2 + z1 * z2
print(v1.cross(v2)) # Cross product = (y1 * z2 - z1 * y2,
                    #                  z1 * x2 - x1 * z2,
                    #                  x1 * y2 - y1 * x2)
print(v3 == v1)
