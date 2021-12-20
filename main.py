class Rectangle:
    b_r = []
    c_r = []

    def __init__(self, b, c):
        self.width = b; type(self).b_r.append(self.width)
        self.length = c; type(self).c_r.append(self.length)

    def square(self):
        return self.width * self.length

    @classmethod
    def total(cls):
        sum_r = []
        n = len(cls.b_r)
        for i in range(0, n):
            sum_r.append(cls.c_r[i]*cls.b_r[i])
        return sum_r


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


A1, A2, A3 = Rectangle(3, 4), Rectangle(2, 3), Rectangle(5, 6)
print(A1.square(), A2.square(), A3.square())

B1, B2, B3 = Square(5), Square(2), Square(3)
print(B1.square(), B2.square(), B3.square())

print(Rectangle.total())
