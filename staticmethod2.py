class A:
    def show(self):
        self.a=10
        print(self.a)
    @staticmethod
    def view():
        A.a=20
        print(A.a)
ob=A()
ob.show()
ob.view()
