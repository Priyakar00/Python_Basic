t=[]
n=int(input('Enter list length:'))
for i in range(n):
    t.append(int(input('Enter list elements:')))
print(t)
print('Sum of array elements is')
max=t[0]
min=t[0]
for i in range(n):
    if max<t[i]:
        max=t[i]
    
print(max,end=' ')    
    
    
