class A:
    def show(self):
        print('Hello show 1')
class B(A):
    def show(self):
        super().show()
        print('hello show 2')
ob=B()
ob.show()
        
