a=int(input('Enter a number:'))#121
n=a
p=0
while(a>0):#121#12#1
    r=a%10#1#2#1
    p=(p*10)+r#1#12#121<--
    a=a//10#12#1#0
if(n==p):
    print('This is palindrom number.')
else:
    print('This is not palindrom number.')
