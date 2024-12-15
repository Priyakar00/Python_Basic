#default argument
'''
def show(a=0,b=0):
    print(a)
    print(b)
show(4,5)
show(8)
show()
'''

#Required argument
'''
def show(a,b):
    print(a)
    print(b)
show(4,5)
show(8)
show()

'''

#Keyword argument
'''
def show(name,roll):
    print('name:',name)
    print('roll:',roll)
show("kolkata",5)
show(roll=4,name="Saltlake")
'''

#variable length
def show(*p):
    #print(p)
    for i in p:
        print(i)
show(1,3,2,34,5,6,7,8,9,90)
