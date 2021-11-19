class A:
    def __init__(self, v):
        self.v = v
    def add_1(self, x):
        self.v += x
        print(self.v)
    def add_2(self, x):
        self.v += x
        print(self.v)

class B(A):

    def __init__(self):
        super(B, self).__init__(0)

    def add(self, x):
        super().add(x)

b = B()
b.add_1(5)  # 3
b.add_2(10)