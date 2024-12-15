'''
def show(a):
    if(a<=5):
        print(a)
        show(a+1)
show(1)
'''
n=int(input('Enter a number: '))
def show(a):
    if(a<=n):
        print(a)
        show(a+1)
show(1)

