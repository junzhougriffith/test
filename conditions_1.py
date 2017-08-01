# here is the student class

class student:
    "here is the student class"
    allage = 0
    def __init__(self, n, a):
        self.studentname = n
        self.age = a

    def get_age(self):
        return self.age

    def increment(self):
        self.age = self.age + 1

bob = student('bob', 22)
bob.increment()

g = bob.__class__('tim', 44)
print(g.__dict__)