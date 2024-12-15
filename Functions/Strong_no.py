def strong(a):
    d=0
    while(a>0):
        b=a%10
        c=1
        for i in range(1,b+1):
            c=c*i
        d=d+c
        a=a//10
    return d
    
a=int(input('Enter no:'))    
y=strong(a)
if(y==a):
    print('This is strong number.')
else:
    print('This is not strong number.')
