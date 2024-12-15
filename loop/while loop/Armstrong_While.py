a=int(input('Enter a number:'))
n=a
b=0
s=0
while(a>0):#153#15#1
    b+=1#1#2#3
    a=a//10#15#1#0
a=n
while(a>0):#153#15#1
    r=a%10#3#5#1
    p=r**b#27#125#1
    s=s+p#27#152#153
    a=a//10#15#1#0
if(s==n):
    print('This is armstrong number')
else:
    print('This is not an armstrong number')
    
