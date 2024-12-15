from tkinter import *
from pymysql import *
from random import *
from form_update_gui import *
root=Tk()
root.minsize(width="500", height="400")
root.maxsize(width="800", height="800")
root.title("Registration Form")

var=IntVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()

var4=StringVar()
var4.set('--select--')

var8 = IntVar()
var8.set(randint(50000,600000))

def show():
    con=connect(host="localhost",user="root",password="",db="form")
    a=con.cursor()
    id=e1.get()
    #print(id)
    name=e2.get()
    #print(name)
    cont=e3.get()
    #print(cont)
    gen=''
    if(var.get()==3):
        gen='Male '
    else:
        gen='Female '
    #print(gen)
    course=var4.get()
    #print(course)
    hob=''
    if(var1.get()==1):
        hob=hob+'Drawing '
    if(var2.get()==1):
        hob=hob+'Gardening '
    if(var3.get()==1):
        hob=hob+'Dancing '
    #print(hob)
    sql="insert into registration values(%s,'%s',%s,'%s','%s','%s')"%(id,name,cont,gen,course,hob)
    
    a.execute(sql)
    con.commit()
    

def cancel():
    var8.set(randint(600000,999999))
    e2.delete(0,END)
    e3.delete(0,END)
    var4.set('--select--')
    c1.deselect()
    c2.deselect()
    c3.deselect()

def close():
    root.destroy()
def update():
    root.destroy()
    update_gui()
l1=Label(root, text='Id:', font=15)
l1.place(x=30, y=30)


el1=Label(root,font=15,textvariable=var8)
el1.place(x=120, y=30)

l2=Label(root, text='Name:', font=15)
l2.place(x=30, y=70)

e2=Entry(root,font=15)
e2.place(x=120, y=70)

l3=Label(root, text='Contact:', font=15)
l3.place(x=30, y=110)

e3=Entry(root,font=15)
e3.place(x=120, y=110)

l4=Label(root, text='Gender:', font=15)
l4.place(x=30, y=150)

r1=Radiobutton(root, variable=var, text='M',font=15, value=3)
r1.place(x=120, y=150)

r2=Radiobutton(root, variable=var, text='F',font=15,value=4)
r2.place(x=170, y=150)

l5=Label(root, text='Course:', font=15)
l5.place(x=30, y=190)

op=OptionMenu(root,var4,'c', 'java', 'python', 'sql')
op.place(x=120, y=190, width=100)

l6=Label(root, text='Hobbies:', font=15)
l6.place(x=30, y=230)

c1=Checkbutton(root, text='Drawing',variable=var1,font=15)
c1.place(x=120,y=230)

c2=Checkbutton(root, text='Gardening',variable=var2,font=15)
c2.place(x=220,y=230)

c3=Checkbutton(root, text='Dancing',variable=var3,font=15)
c3.place(x=350,y=230)

b1=Button(root, text='Submit', font=15, bd=8,command=show)
b1.place(x=30, y=290)

b2=Button(root, text='Cancel', font=15, bd=8,command=cancel)
b2.place(x=150, y=290)

b3=Button(root, text='Close', font=15, bd=8, command=close)
b3.place(x=280, y=290)

b4=Button(root, text='Update', font=15, bd=8, command=update)
b4.place(x=380, y=290)

root.mainloop()



