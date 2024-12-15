t=[]
row=int(input('Enter row: '))
col=int(input('Enter col: '))
print('Enter elements: ')
for i in range(row):
    w=[]
    for j in range(col):
        b=int(input())
        w.append(b)
    t.append(w)
print('matrix is: ')
for i in t:
    for j in i:
        print(j,end=' ')
    print()

print('Transpose of a matrix is: ')
t1=[]
for i in range(col):
    w1=[]
    for j in range(row):
        w1.append(t[j][i])
    t1.append(w1)
for i in t1:
    for j in i:
        print(j,end=' ')
    print()
