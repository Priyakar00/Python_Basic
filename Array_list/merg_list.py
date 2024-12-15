t=[]
n=int(input('Enter 1 length: '))
print('Enter elements: ')
for i in range(n):
    b=int(input())
    t.append(b)
print(' 1 list is: ')
print(t)

t1=[]
n1=int(input('Enter 2 length: '))
print('Enter elements: ')
for i in range(n1):
    b1=int(input())
    t1.append(b1)
print('2 list is: ')
print(t1)

print("Merge array: ")
x=[]
for i in range(n):
    x.append(t[i])

for i in range(n1):
    x.append(t1[i])
print(x)
    
