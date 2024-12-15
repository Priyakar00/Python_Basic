class A:
    def __init__(self):
        self.a=0
        A.b=0
    def increment(self):
        A.b+=1
        self.a=A.b
    def show(self):
        print(self.a,' ',A.b)

ob1=A()
ob2=A()
ob3=A()

ob1.increment()
ob2.increment()
ob3.increment()

ob1.show()
ob2.show()
ob3.show()
