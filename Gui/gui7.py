from tkinter import *
root=Tk()
root.minsize(width="350", height="350")
root.maxsize(width="800", height="800")
root.title("Hello")

var = StringVar()
s =""
def show(a):
    global s
    s = s+str(a)
    var.set(s)

l1=Label(root,textvariable=var,font=15)
l1.place(x=0, y=10)

c1=Button(root, text="1",font=10,bd=8,command=lambda:show(1))
c1.place(x=0, y=50)

c2=Button(root, text="2",font=10,bd=8,command=lambda:show(2))
c2.place(x=30, y=50)

c3=Button(root, text="3",font=10,bd=8,command=lambda:show(3))
c3.place(x=60, y=50)

c4=Button(root, text="4",font=10,bd=8,command=lambda:show(4))
c4.place(x=90, y=50)

root.mainloop()
