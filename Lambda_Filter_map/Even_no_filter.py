'''
#using function

def even(a):
    for i in a:
        if(i%2==0):
            print(i)        
a = [1,2,3,4,5,6]
even(a)

#using filter

def even(a):
    if(a%2==0):
        return True      
a = [1,2,3,4,5,6]
lt = filter(even,a)
print(lt)
for i in lt:
    print(i,end = " ")
'''
#using lambda funtion and filter

even = lambda a:(a%2==0)
a = [1,2,3,4,5,6]
print(a)
lt = filter(even,a)
print('Even no are: ')
#print(lt)
for i in lt:
    print(i,end = " ")
