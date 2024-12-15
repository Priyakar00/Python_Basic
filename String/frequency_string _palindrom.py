a=str(input('Enter a string '))
print(a)
b=a.split()
#print(b)
n=len(b)
#print(n)
count=0
for i in range (n):
    c=b[i]
    #print(c)
    d=c[::-1]
    #print(d)
    if(d==c):
        count+=1
print('Frequency:',count)
