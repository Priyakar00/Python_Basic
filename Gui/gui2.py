from tkinter import *
root=Tk()
root.minsize(width=450, height=50)
root.maxsize(width=800, height=800)
root.title('my gui 1')


def show():
    a = n1.get()
    print(a)
    n1.delete(0,END)
n=Label(root, text="Name",fg="red",bg="yellow",font = 18)
n.place(x=50,y=50)


n1=Entry(root,font=18)
n1.place(x=200,y=50)


n2=Button(root, text="Ok",font=18,bd=8,width=10,command=show)
n2.place(x=190,y=130)

root.mainloop()
