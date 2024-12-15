print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division')
a=int(input('Enter your choice:'))
if(a==1):
    b=int(input('Enter one value:'))
    c=int(input('Enter another value:'))
    d=b+c
    print('Addition:',d)
elif(a==2):
    b1=int(input('Enter one value:'))
    c1=int(input('Enter another value:'))
    d1=b1-c1
    print('Subtraction:',d1)
elif(a==3):
    b3=int(input('Enter one value:'))
    c3=int(input('Enter another value:'))
    d3=b3*c3
    print('Multiplication:',d3)
elif(a==4):
    b4=int(input('Enter one value:'))
    c4=int(input('Enter another value:'))
    d4=b4/c4
    print('Division:',d4)
else:
    print('Wrong choice!!!')
