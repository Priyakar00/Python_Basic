sqr=lambda a:a**2
a=[1,2,3,4,5,6,7]
print(a)
lt=map(sqr,a)
print('Square: ')
for i in lt:
    print(i,end=' ')
