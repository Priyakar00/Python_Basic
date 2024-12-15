t=[]
n=int(input('Enter length: '))
print('Enter elements: ')
for i in range(n):
    b=int(input())
    t.append(b)
print('list is: ')
print(t)

pos=int(input("Enter position where you insert the value: "))
val=int(input("Enter the value:"))
t.append(t[n-1])
print(t)
for i in range(n,pos-1,-1):
    t[i]=t[i-1]

t[pos-1]=val           
a=[]
for i in range(n+1):
    a.append(t[i])
print(a)
