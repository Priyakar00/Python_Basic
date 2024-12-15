t=[]
n=int(input('Enter length: '))
print('Enter elements: ')
for i in range(n):
    b=int(input())
    t.append(b)
print('list is: ')
print(t)
pos=int(input('Enter the position to delete!!'))
for i in range(pos-1,n-1):
    t[i]=t[i+1]
x=[]
for i in range(n-1):
    x.append(t[i])
print(x)
