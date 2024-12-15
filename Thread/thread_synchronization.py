import threading
lock=threading.Lock()
class display():
    def wish(self,name):
        for i in range(1,11):
            print("gm ",name)
            
class mythread(threading.Thread):
    def __init__(self,d,n):
        threading.Thread.__init__(self)
        self.d=d
        self.n=n
    def run(self):
        lock.acquire()
        self.d.wish(self.n)
        lock.release()
d=display()
t1=mythread(d,"ABC")
t2=mythread(d,"XYZ")

t1.start()
t2.start()
