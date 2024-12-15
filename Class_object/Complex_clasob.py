'''
class complex:
    def set(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print('Complex no: ',self.a,'+',self.b,'i')

c1=complex()
c1.set(10,20)
c2=complex()
c2.set(5,7)
c1.show()
c2.show()
'''        

class complex:
    def set(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,'+',self.b,'i')
    def add(self,p):
        c4=complex()
        c4.a=self.a+p.a
        c4.b=self.b+p.b
        return c4
        

c1=complex()
c1.set(10,20)
c2=complex()
c2.set(5,7)
c3=complex()
c3=c1.add(c2)
c1.show()
c2.show()
c3.show()
