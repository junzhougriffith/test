##////////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Implement a Fraction class which allows the following statements to execute //
##///////////////////////////////////////////////////////////////////////////////


class Fraction:

    def __init__(self, x, y):
        self.a = x
        self.b = y
        if y == 0:
            print("Divide by zero")
            exit()

    def __str__(self):
        return str(self.a) + '/' + str(self.b)

    def __add__(self, fx):
        f = Fraction(self.a * fx.b + fx.a * self.b,  self.b * fx.b)
        m = abs(f.a)
        for n in range(2, m + 1):
            if f.a % n == f.b % n == 0:
               f.a //= n
               f.b //= n
        return f

    def __sub__(self, fx):
        f = Fraction(self.a * fx.b - fx.a * self.b, self.b * fx.b)
        m = abs(f.a)
        for n1 in range(2, m+1):
            if f.a % n1 == f.b % n1 == 0:
                f.a //= n1
                f.b //= n1
        return f

    def __truediv__(self, fx):
        f = Fraction(self.a * fx.b, self.b * fx.a)
        m = abs(f.a)
        for n2 in range(2, m + 1):
            if f.a % n2 == f.b % n2 == 0:
                f.a //= n2
                f.b //= n2
        return f

    def __mul__(self, fx):
        f = Fraction(self.a * fx.a, self.b * fx.b)
        m = abs(f.a)
        for n2 in range(2, m + 1):
            if f.a % n2 == f.b % n2 == 0:
                f.a //= n2
                f.b //= n2
        return f

    def __mod__(self, fx):
        f = Fraction(self.a, self.b)
        if self.a * fx.b >= self.b * fx.a:
            return f - fx
        return f

    def __eq__(self, fx):
        return self.a * fx.b == self.b *  fx.a
f1 = Fraction(int(input()), int(input()))
f2 = Fraction(int(input()), int(input()))
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 / f2)
print(f1 * f2)
print(f1 % f2)
print(f1 + f2 / f1 - f2)
print(f1 == f1)
