t=[]
n=int(input('Enter list length:'))
for i in range(n):
    t.append(int(input('Enter list elements:')))
print(t)
print('Sum of array elements is')
a=0
for i in range(n):
    a=a+t[i]
print(a,end=' ')    
    
    
