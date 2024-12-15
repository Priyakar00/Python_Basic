from tkinter import *
root=Tk()
root.minsize(width="400", height="450")
root.maxsize(width="800", height="800")
root.title("Hello")

var=StringVar()
s=''
def show(a):
    global s
    s=s+str(a)
    var.set(s)
def calculate():
    global s
    p=e1.get()
    q=eval(p)
    #print(q)
    s=str(q)
    e1.delete(0,END)
    e1.insert(0,s)

    
def clear():
    global s
    s=""
    e1.delete(0,END)

e1=Entry(root,font=18,textvariable=var)
e1.place(x=10,y=10,width=380,height=60)
#
b1=Button(root, text='7',font=10,bd=8,width=7,command=lambda:show(7))
b1.place(x=10, y=80)

b2=Button(root, text='8',font=10,bd=8,width=7,command=lambda:show(8))
b2.place(x=100, y=80)

b3=Button(root, text='9',font=10,bd=8,width=7,command=lambda:show(9))
b3.place(x=200, y=80)

b4=Button(root, text='+',font=10,bd=8,width=7,command=lambda:show('+'))
b4.place(x=300, y=80)
#
b5=Button(root, text='4',font=10,bd=8,width=7,command=lambda:show(4))
b5.place(x=10, y=140)

b6=Button(root, text='5',font=10,bd=8,width=7,command=lambda:show(5))
b6.place(x=100, y=140)

b7=Button(root, text='6',font=10,bd=8,width=7,command=lambda:show(6))
b7.place(x=200, y=140)

b8=Button(root, text='-',font=10,bd=8,width=7,command=lambda:show('-'))
b8.place(x=300, y=140)
#
b9=Button(root, text='1',font=10,bd=8,width=7,command=lambda:show(1))
b9.place(x=10, y=200)

b10=Button(root, text='2',font=10,bd=8,width=7,command=lambda:show(2))
b10.place(x=100, y=200)

b11=Button(root, text='3',font=10,bd=8,width=7,command=lambda:show(3))
b11.place(x=200, y=200)

b12=Button(root, text='*',font=10,bd=8,width=7,command=lambda:show('*'))
b12.place(x=300, y=200)
#
b13=Button(root, text='c',font=10,bd=8,width=7,command=clear)
b13.place(x=10, y=260)

b14=Button(root, text='0',font=10,bd=8,width=7,command=lambda:show(0))
b14.place(x=100, y=260)

b15=Button(root, text='=',font=10,bd=8,width=7,command=calculate)
b15.place(x=200, y=260)

b16=Button(root, text='/',font=10,bd=8,width=7,command=lambda:show('/'))
b16.place(x=300, y=260)
root.mainloop()
