a=[]
f=0
n=int(input('Enter list length:'))
for i in range(n):
    a.append(int(input('Enter list elements:')))
print(a)    
#print('Which element do you want to search?')
b=int(input('Which element do you want to search?'))
for i in range(n):
    if(b==a[i]):
        print('Found in position',i+1)
        f=1
        break
if(f==0):
    print('Data not found')
