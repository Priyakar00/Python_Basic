class A:
    def setdata(self):
        self.n=str(input('Enter name: '))
        self.r=int(input('Enter roll: '))
        self.m=int(input('Enter marks: '))
class B(A):
    def show(self):
        print('name:',self.n)
        print('roll:',self.r)
        print('marks:',self.m)

ob=B()
ob.setdata()
ob.show()
