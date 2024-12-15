'''
class test:
    def car(self):
        print('Audi car')
ob=test()
ob.car()

def fast_car(self):
    print('audi car')
test.car=fast_car
ob1=test()
ob1.car()
'''
class A:
    def show(self):
        print('Hello show 1')
ob=A()
ob.show()

def B_A(self):
    print('Hello show 2')
A.show=B_A
ob.show()
