class A:
    def show(self):
        print('hello show')
    @staticmethod
    def view():
        print('hello view')
ob=A()
ob.show()
ob.view()
A.view()
