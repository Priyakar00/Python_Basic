from tkinter import *
root=Tk()
root.minsize(width="450", height="450")
root.maxsize(width="800", height="800")
root.title("Hello")

def add():
    a=int(e1.get())#a=e1.get()
    b=int(e2.get())#b=e2.get()
    #c=int(a)+int(b)
    c=a+b
    e3.insert(0,c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    d=a-b
    e3.insert(0,d)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    e=a*b
    e3.insert(0,e)
def div():
    a=int(e1.get())
    b=int(e2.get())
    f=a/b
    e3.insert(0,f)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
def exit():
    root.destroy()
    


l1=Label(root, text='First No:',font=10)
l1.place(x=30, y=30)

e1=Entry(root, font=10)
e1.place(x=150, y=30)

l2=Label(root, text='Last No:',font=10)
l2.place(x=30, y=80)

e2=Entry(root, font=10)
e2.place(x=150, y=80)

b1=Button(root, text='+', font=10,bd=8,command=add)
b1.place(x=150, y=130)

b2=Button(root, text='-', font=10,bd=8,command=sub)
b2.place(x=190, y=130)

b3=Button(root, text='*', font=10,bd=8,command=mul)
b3.place(x=230, y=130)

b4=Button(root, text='/', font=10,bd=8,command=div)
b4.place(x=270, y=130)

l3=Label(root, text='Result:',font=10)
l3.place(x=30, y=200)

e3=Entry(root, font=10)
e3.place(x=150, y=200)

b5=Button(root, text='Clear', font=10,bd=8,command=clear)
b5.place(x=130, y=250)

b6=Button(root, text='Exit', font=10,bd=8,command=exit)
b6.place(x=200, y=250)

root.mainloop()
