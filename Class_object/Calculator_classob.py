class Add:
    def set(self):
        self.a=int(input('Enter a number: '))
        self.b=int(input('Enter another number: '))
    def sum(self):
        self.c=self.a+self.b
    def show(self):
        print('Sum= ',self.c)
        
class Subtract:
    def set(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        self.c=self.a-self.b
    def show(self):
        print('Subtraction= ',self.c)

class Multiplication:
    def set(self):
        self.a=int(input('Enter a number: '))
        self.b=int(input('Enter another number: '))
    def mul(self):
        self.c=self.a*self.b
    def show(self):
        print('Multiplication= ',self.c)

class Division:
    def set(self,a,b):
        self.a=a
        self.b=b
    def div(self):
        self.c=self.a+self.b
    def show(self):
        print('Sum= ',self.c)
a1=Add()
a1.set()
a1.sum()
a1.show()

s1=Subtract()
s1.set(7,2)
s1.sub()
s1.show()

m1=Multiplication()
m1.set()
m1.mul()
m1.show()

d1=Division()
d1.set(5,2)
d1.div()
d1.show()
