n=int(input('Enter a no'))
m=0
for i in range(1,n):
    if(n%i==0):
        m+=1
if(m==2):
    print('This is prime number')
else:
    print('This is not a prime number')
