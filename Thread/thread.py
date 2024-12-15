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
ob=A()
ob1=B()
ob.start()
ob1.start()
