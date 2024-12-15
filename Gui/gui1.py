from tkinter import *

root = Tk()

root.minsize(width=400,height=400)
root.maxsize(width=800,height=800)
root.title("my gui")

#pack , grid , place
'''
b1 = Button(root,text="click")
b1.pack()
b2= Button(root,text="ok")
b2.pack()


b1 = Button(root,text="click")
b1.grid(row=0,column=0)
b2= Button(root,text="ok")
b2.grid(row=0,column=10)
'''

b1 = Button(root,text="click")
b1.place(x=0,y=0)
b2= Button(root,text="ok")
b2.place(x=50,y=250)

root.mainloop()
