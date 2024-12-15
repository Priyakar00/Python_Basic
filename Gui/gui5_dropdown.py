from tkinter import *
root=Tk()
root.minsize(width=350, height=350)
root.maxsize(width=800, height=800)
root.title('DropDown')

var=StringVar()
var.set("---SELECT--")

def show():
    a=var.get()
    print(a)

l1=Label(root, text='Course:', font=18)
l1.place(x=50, y=50)

op=OptionMenu(root,var,"C","C++","JAVA","PYTHON")
op.place(x=190, y=50,width=70, height=60)

b1=Button(root, text='Submit',font=18, bd=8,command=show)
b1.place(x=150, y=200)

root.mainloop()
