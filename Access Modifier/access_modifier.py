class A:
    def show(self):
        print("Public function")
    def _show(self):
        print("Protected function")
    def __show(self):
        print("Private function")
ob=A()
ob.show()
ob._show()
#ob.__show()
ob._A__show()
