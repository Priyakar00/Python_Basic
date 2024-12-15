class A:
    def set(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
    def show(self):
        print('Sum= ',self.c)
o1=A()
o1.set(10,20)
o1.add()
o1.show()
        
