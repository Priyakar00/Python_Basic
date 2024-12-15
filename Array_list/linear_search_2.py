a=[]
n=int(input('Enter list length:'))
for i in range(n):
    a.append(int(input('Enter list elements:')))
print(a)    
#print('Which element do you want to search?')
b=int(input('Which element do you want to search?'))
if(b in a):
    print('Data found')
else:
    print('Data not found')
