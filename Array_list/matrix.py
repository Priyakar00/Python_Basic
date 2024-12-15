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
#diagonal 1
print('diagonal matrix is: ')
for i in range(row):
    for j in range(col):
        if(i==j):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
#diagonal 2
print('diagonal matrix is: ')

for i in range(row):
    for j in range(col):
        if(i+j==col-1):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
#diagonal 3
    print('diagonal matrix is: ')
for i in range(row):
    for j in range(col):
        if(i==j):
            print(t[i][j],end=' ')
        else:
            print(0,end=' ')
    print()

#diagonal 4
print('diagonal matrix is: ')
for i in range(row):
    for j in range(col):
        if(i==j or i+j==col-1):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
    print()
