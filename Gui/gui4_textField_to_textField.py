from tkinter import *
root=Tk()
root.minsize(width=450, height=350)
root.maxsize(width=800, height=800)
root.title('my gui 1')


def show():
    a = e1.get()
    #print(a)
    e1.delete(0,END)
    e2.delete(0,END)
    e2.insert(0,a)
l1=Label(root, text="Name",fg="red",bg="yellow")
l1.place(x=50,y=50)

l2=Label(root, text="Name",fg="white",bg="blue")
l2.place(x=50,y=230)


e1=Entry(root,font=18)
e1.place(x=200,y=50)


e2=Entry(root,font=18)
e2.place(x=190,y=230)


b1=Button(root, text="Ok",font=18,bd=8,width=10,command=show)
b1.place(x=200,y=150)

root.mainloop()
