class A:
    def shape(self,a=0,b=0):
        self.a=a
        self.b=b
        print(self.a,' ',self.b)
ob=A()
ob.shape(10,20)
ob.shape(10)
ob.shape()
