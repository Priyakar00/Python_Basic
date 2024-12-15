'''
class A:
    def __init__(self):
        self.a=0
    def increment(self):
        self.a+=1
    def show(self):
        print(self.a)

ob1=A()
ob2=A()
ob3=A()

ob1.increment()
ob1.increment()
ob1.increment()
ob2.increment()
ob2.increment()
ob3.show()
ob1.show()
ob2.show()
'''
class A:
    def __init__(self):
        A.a=0
    def increment(self):
        A.a+=1
    def show(self):
        print(A.a)

ob1=A()
ob2=A()
ob3=A()

ob1.increment()
ob1.increment()
ob1.increment()
ob2.increment()
ob2.increment()
ob3.show()
ob1.show()
ob2.show()
