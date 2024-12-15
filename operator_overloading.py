class complex:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,'+',self.b,'i')
    def __add__(self,p):
        c4=complex()
        c4.a=self.a+p.a
        c4.b=self.b+p.b
        return c4

c1=complex(10,20)
c2=complex(5,7)
c3=complex()

c3=c1+c2

c1.show()
c2.show()
c3.show()
