from threading import *
import time
#import threading--->then use threading.Thread
class A(Thread):#--->to extend
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("hello",i)
class B(Thread):
    def run(self):
        for i in range(10):
            time.sleep(2)
            print("Hi",i)
ob=A()
ob1=B()
ob.start()
ob1.start()
