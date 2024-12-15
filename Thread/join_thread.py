from threading import *
#import threading--->then use threading.Thread
class A(Thread):#--->to extend
    def run(self):
        for i in range(10):
            print("hello",i)
class B(Thread):
    def run(self):
        for i in range(10):
            print("Hi",i)
class C(Thread):
    def run(self):
        for i in range(10):
            print("Welcome",i)
ob=A()
ob1=B()
ob2=C()
ob.start()
ob.join()#--->same as java
ob1.start()
ob2.start()
