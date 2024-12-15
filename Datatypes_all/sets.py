#sets
#It is an unordered collection of unique elements
#1.creation
x=set()
print(type(x))
print(x)
x=set([1,2,3,4])#printing list as set
print(x)

print('--'*20)

#add values in a set
x=set()
x.add(10)
x.add(20)
x.add(30)
x.add(40)
print(x)

print('--'*20)

#to remove duplicate from given list
lst=[1,2,3,4,5,6,1,1,2,3,4,2,1,7,8]
x=set(lst)
print(x)
