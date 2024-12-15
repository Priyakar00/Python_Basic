class A:
    def set(self):
        self.a=int(input('Enter a number: '))
        self.b=int(input('Enter another number: '))
    def add(self):
        self.c=self.a+self.b
    def show(self):
        print('sum= ',self.c)
ob1=A()
ob1.set()
ob1.add()
ob1.show()
