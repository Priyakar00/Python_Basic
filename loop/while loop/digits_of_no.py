n=int(input('Enter a no: '))
c=0
while(n>0):
    d=n%10
    c+=1
    print(d,end=' ')
    n=n//10

