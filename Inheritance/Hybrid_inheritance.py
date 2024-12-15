class A:
    def setdata(self):
        self.n=str(input('Enter name: '))
        self.r=int(input('Enter roll: '))

class B(A):
    def marks(self):
        self.m=int(input('Enter physics marks: '))
        self.p=int(input('Enter chemistry marks: '))
        self.q=int(input('Enter math marks: '))
        self.t=(self.m+self.p+self.q)
        self.a=(self.t)/3

class C(A):
    def sports(self):
        self.m=int(input('Enter 1st round point: '))
        self.p=int(input('Enter 2nd round point: '))
        self.q=int(input('Enter 3rd round point: '))
        self.t1=(self.m+self.p+self.q)
        self.a1=(self.t1)/3
    
class D(B,C):
    def show(self):
        print('Name: ',self.n)
        print('Roll: ',self.r)
        print('Total marks: ',self.t)
        print('Average marks: ',self.a)
        print('Total point: ',self.t1)
        print('Average point: ',self.a1)
ob=D()
ob.setdata()
ob.marks()
ob.sports()
ob.show()
