from tkinter import *
root=Tk()
root.minsize(width=350, height=350)
root.maxsize(width=800, height=800)
root.title('Radio button')

var1=IntVar()
var2=IntVar()
var3 = IntVar()
var4 = IntVar()

def show():
    #a=var1.get()
    #print(a)
    s=''
    if(var1.get()==1):
        s=s+'c '
    if(var2.get()==1):
        s=s+'java '
    if(var3.get()==1):
        s=s+'python '
    if(var4.get()==1):
        s=s+'html '
    print(s)
    '''
    if(a==3):
        print('Male')
    else: 
        print('Female')
    '''
l1=Label(root, text='Course:')
l1.place(x=10, y=50)

c1 = Checkbutton(root,text = "c" , variable = var1)
c1.place(x=10,y=100)
c2 = Checkbutton(root,text = "java" , variable = var2)
c2.place(x=60,y=100)
c3 = Checkbutton(root,text = "python" , variable = var3)
c3.place(x=110,y=100)
c4 = Checkbutton(root,text = "html" , variable = var4)
c4.place(x=160,y=100)

b1=Button(root, text='Submit',font=18, bd=8,command=show )
b1.place(x=150, y=250)

root.mainloop()
