import threading#--->then use threading.Thread
class A(threading.Thread):#--->to extend
    def run(self):
        for i in range(10):
            print(threading.currentThread().getName())
            print("hello",i)
class B(threading.Thread):
    def run(self):
        for i in range(10):
            print(threading.currentThread().getName())
            print("Hi",i)
ob=A()
ob1=B()
ob.start()
ob1.start()
