class A:
    def set(self,a,b):
        self.a=a
        self.b=b
    def multi(self):
        self.c=self.a*self.b
    def show(self):
        print('Multiplication: ',self.c)
a1=A()
a1.set(20,5)
a1.multi()
a1.show()

a2=A()
a2.set(5,7)
a2.multi()
a2.show()
