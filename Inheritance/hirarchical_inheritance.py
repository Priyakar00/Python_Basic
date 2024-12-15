class A:
    def input(self):
        self.n=str(input('Enter name: '))
        self.r=int(input('Enter roll: '))
        self.c=str(input('Enter course: '))
   
class B(A):
    def marks(self):
        self.m=int(input('Enter math marks: '))
        self.c=int(input('Enter che marks: '))
        self.p=int(input('Enter phy marks: '))
        self.t=self.m+self.c+self.p
        self.a=(self.t)/3
    def show(self):
        print('Name: ',self.n)
        print('Roll: ',self.r)
        print('Course: ',self.c)
        print('Total marks: ',self.t)
        print('Marks average: ',self.a)

class c(A):
    def marks(self):
        self.m=int(input('Enter math marks: '))
        self.c=int(input('Enter che marks: '))
        self.p=int(input('Enter phy marks: '))
        self.t=self.m+self.c+self.p
        self.a=(self.t)/3
    def show(self):
        print('Name: ',self.n)
        print('Roll: ',self.r)
        print('Course: ',self.c)
        print('Total marks: ',self.t)
        print('Marks average: ',self.a)
        
ob1=B()
ob1.input()
ob1.marks()
ob1.show()
ob2=c()
ob2.input()
ob2.marks()
ob2.show()
        
    
    
