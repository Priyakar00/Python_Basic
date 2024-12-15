t=[]
n=int(input('Enter list length:'))
for i in range(n):
    b=int(input('Enter list element:'))
    t.append(b)
print(t)
print('N to 1 list element')
for i in range(n-1,-1,-1):
    print(t[i],end=' ')
print()
