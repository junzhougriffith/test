##///////////////////////// PROBLEM STATEMENT ///////////////////////////////////
## Implement a Circle class where a circle is defined by the location of its   //
## centre (x,y) and radius. Your class should allow the code below to execute. //
##///////////////////////////////////////////////////////////////////////////////

class Circle:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.r = c

    def __str__(self):
        return "(%d, %d), %d" %(self.x, self.y, self.r)

    def circumference(self):
        return 'C = %.2f' %(2*3.1416*self.r)  'C=' + str(round(2*3.1416*self.r, 2))

    def area(self):
        return 'A =' + str(round(3.1416*self.r**2, 2))

    def intersect(self, cir):
        d = ((self.x - cir.x) ** 2 + (self.y - cir.y) ** 2) ** 0.5
        return d < (self.r + cir.r)

    def contains(self, cir):
        d = ((self.x - cir.x) ** 2 + (self.y - cir.y) ** 2) ** 0.5
        return d <= (self.r - cir.r)

    def __eq__(self, cir):
        return self.x == cir.x and self.y == cir.y and self.r == cir.r


c1 = Circle(int(input()), int(input()), int(input()))
c2 = Circle(int(input()), int(input()), int(input()))
c3 = Circle(c1.x, c1.y, c1.r)
print(c1)
print(c1.circumference())
print(c1.area())
print(c1.intersect(c2))
print(c1.contains(c2))
print(c3 == c1)
print('hello')
print(a = 1)
print(True)
