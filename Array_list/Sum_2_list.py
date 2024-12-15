t=[]
n=int(input('Enter array length'))
for i in range(n):
    t.append(int(input('Enter 1st array elements')))
print(t)
print()
t1=[]
for i in range(n):
    t1.append(int(input('Enter 2nd array elements')))
print(t1)
print()
print('Sum of two array is:')
t2=[]
for i in range(n):
    t2.append(t[i]+t1[i])
print(t2)
