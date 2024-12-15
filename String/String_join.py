a=str(input('Enter a string:'))
print(a)
r=a.split()
print(r)
n=len(r)
p=""
for i in range(0,n-1):
    m=r[i][0]
    print(m)
    p=p+m+'.'
print(p)
d=r[n-1]
p=p+d[0] #m.s.d
#p = p+r[n-1] #m.s.dhoni
print(p)
