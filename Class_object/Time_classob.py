class time:
    def set(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def show(self):
        print(self.a,':',self.b,':',self.c)
        
    def add(self,p):
        t4=time()
        '''
        t4.a=self.a+p.a+1
        t4.b=(self.b+p.b)//60+10
        t4.c=(self.c+p.c)%60
        '''

        m=(self.c+p.c)%60
        n=(self.c+p.c)//60
        i=(self.b+p.b)%60
        j=(self.b+p.b)//60
        t4.c=m
        t4.b=n+i
        t4.a=self.a+p.a+j
        return t4

t1=time()
t2=time()
t3=time()

t1.set(10,20,40)
t2.set(1,50,25)

t3=t1.add(t2)

t1.show()
t2.show()
t3.show()
