import zope.interface
class Parent(zope.interface.Interface):
    def speed(self,a):
        print("Parent speed",a)
@zope.interface.implementer(Parent)
class Child:
    def speed(self,a):
        print("child speed",a)
c=Child()
c.speed(10)

