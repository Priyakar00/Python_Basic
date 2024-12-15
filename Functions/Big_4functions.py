
print('1.Check the no is Strong or not')
print('2.Check the no is Armstrong or not')
print('3.Check the no is Prime or not')
print('4.Check the no is Perfect or not')
print('5.Check the no is Palindrom or not')
print('6.Check the Fibonacci series')
n=int(input('Enter your choice: '))

#strong number function HRHA
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

#armstrong number funtion HRHA
def armstrong(a):
    b=0
    s=0
    x=a
    while(a>0):
        b+=1
        a=a//10
    a=x
    while(a>0):
        c=a%10
        d=1
        for i in range(1,b+1):
            d=d*c
        s=s+d
        a=a//10
    return s

#prime no funtion HRHA
def prime(a):
    b=0
    for i in range(1,a+1):
        if(a%i==0):
            b+=1
    return b

#perfect no funtion HRHA
def perfect(a):
    b=0
    for i in range(1,a):
        if(a%i==0):
            b=b+i
    return b

#palindrom function HRHA
def palindrom(a):
    p=0
    while(a>0):
        b=a%10
        p=(p*10)+b
        a=a//10
    return p

#fibonacci function NRHA
def fibonacci(a):
    n=0
    b=1
    for i in range(1,a+1):
        t=n
        n=b
        print(t,end=' ')
        b=n+t

if(n==1):
    a=int(input('Enter a number: '))
    y=strong(a)
    if(y==a):
        print('This is strong number.')
    else:
        print('This is not strong number.')
        
elif(n==2):
    a=int(input('Enter a nuumber: '))
    y=armstrong(a)
    if(y==a):
        print('This is armstrong number.')
    else:
        print('This is not armstrong number.')
        
elif(n==3):
    a=int(input('Enter a nuumber: '))
    y=prime(a)
    if(y==2):
        print('This is prime number.')
    else:
        print('This is not prime number.')
        
elif(n==4):
    a=int(input('Enter a nuumber: '))
    y=perfect(a)
    if(y==a):
        print('This is prtfect number.')
    else:
        print('This is not perfect number.')       

elif(n==5):
    a=int(input('Enter a nuumber: '))
    y=palindrom(a)
    if(y==a):
        print('This is palindrom number.')
    else:
        print('This is not palindrom number.')

elif(n==6):
    a=int(input('Enter a nuumber: '))
    fibonacci(a)
else:
    print('Wrong choice!!')
