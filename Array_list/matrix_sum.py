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
print('1st matrix is: ')
for i in t:
    for j in i:
        print(j,end=' ')
    print()

print('Enter 2nd matix elements: ')
t1=[]
for i1 in range(row):
    w1=[]
    for j1 in range(col):
        b1=int(input())
        w1.append(b1)
    t1.append(w1)
print('2nd matrix is: ')
for i1 in t1:
    for j1 in i1:
        print(j1,end=' ')
    print()

t2=[]
for i in range(row):
    w2=[]
    for j in range(col):
        w2.append(t[i][j]+t1[i][j])
    t2.append(w2)
        
print('sum of two matrix is: ')
for i in t2:
    for j in i:
        print(j,end=' ')
    print()
        
        

