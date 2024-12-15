a=[]
f=0
n=int(input('Enter list length:'))
for i in range(n):
    a.append(int(input('Enter list elements:')))
print(a)    
b=int(input('Which element do you want to delete?'))
for i in range(n):
    if(b==a[i]):
        for j in range(i,n-1):
            a[j]=a[j+1]
        for k in range(0,n-1):
            print(a[k],end=' ')
        f=1
        break
    
if(f==0):
    print('Data not found')

#for i in range(0,n-1):
    
