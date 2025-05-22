# MRO - Method Resolution Order

class X:
    def __init__(self):
        print('X init')
class Y:
    def __init__(self):
        print('y init')
class Z:
    def __init__(self):
        print('Z init')
class A(X, Y):
    def __init__(self):
        super().__init__()

class B(Y, Z):
    def __init__(self):
        super().__init__()
    
class M(B, A, Z):
    def __init__(self):
        super().__init__()
print(M.__mro__)




