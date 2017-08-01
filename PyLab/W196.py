##///////////////////////////////// PROBLEM STATEMENT /////////////////////////////////
## Implement a ComplexNumber class which allows the following statements to execute. //
## The arithmetic rules for complex numbers are (i is the square root of -1):        //
##   (a + b * i) + (c + d * i) = (a + c) + (b + d) * i                               //
##   (a + b * i) - (c + d * i) = (a - c) + (b - d) * i                               //
##   (a + b * i) * (c + d * i) = (a * c - b * d) + (a * d + b * c) * i               //
##   (a + b * i) / (c + d * i) = (a * c + b * d) / (c * c + d * d) +                 //
##                                   ((b * c - a * d) / (c * c + d * d)) * i         //
##/////////////////////////////////////////////////////////////////////////////////////
class ComplexNumber:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return '%.2f'%self.a + '+' + '%.2f'%self.b + 'i'

    def __add__(self, other):
        f = ComplexNumber(self.a + other.a, self.b + other.b)
        return f

    def __sub__(self, other):
        f = ComplexNumber(self.a - other.a, self.b - other.b)
        return f

    def __truediv__(self, other):
        f = ComplexNumber((self.a * other.a + self.b * other.b)/ (other.a * other.a + other.b * other.b), (self.b * other.a - self.a * other.b)/ (other.a * other.a + other.b * other.b))
        return  f

    def __mul__(self, other):
        f = ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        return f

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
c1 = ComplexNumber(int(input()), int(input()))
c2 = ComplexNumber(int(input()), int(input()))
c3 = ComplexNumber(c1.a, c1.b)

print(c1 + c2)
print(c1 - c2)
print(c1 / c2)
print(c1 * c2)
print(c1 + c2 / c1 - c2)
print(c3 == c1)
