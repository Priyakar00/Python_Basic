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
class C(B):
    def show(self):
        print('Name: ',self.n)
        print('Roll: ',self.r)
        print('Total marks: ',self.t)
        print('Average: ',self.a)

ob=C()
ob.setdata()
ob.marks()
ob.show()
