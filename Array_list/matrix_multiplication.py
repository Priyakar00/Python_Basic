t=[]
r1=int(input('Enter 1st matrix row: '))
c1=int(input('Enter 1st matrix col: '))
print('Enter elements: ')
for i in range(r1):
    w=[]
    for j in range(c1):
        b=int(input())
        w.append(b)
    t.append(w)
print('1st matrix is: ')
for i in t:
    for j in i:
        print(j,end=' ')
    print()

r2=int(input('Enter 2nd matrix row: '))
c2=int(input('Enter 2nd matrix col: '))

print('Enter 2nd matix elements: ')
t1=[]
for i1 in range(r2):
    w1=[]
    for j1 in range(c2):
        b1=int(input())
        w1.append(b1)
    t1.append(w1)
print('2nd matrix is: ')
for i in t1:
    for j in i:
        print(j,end=' ')
    print()



t2=[]
for i in range(r1):
    w2=[]
    for j in range(c2):
        k=0
        for p in range(c1):
            k=k+(t[i][p]*t1[p][j])
        w2.append(k)
    t2.append(w2)
print('matrix multiplication: ')
for i in t2:
    for j in i:
        print(j,end=' ')
    print()
    


        
        
        
