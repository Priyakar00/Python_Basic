#string properties
#1)immutability
#2)arithmetic operation on string(+,*)

#1
s='Hello '
s=s+'world'
print(s)

print("--"*20)
#2
p='hello'
q='world'
print(p+q)
s=p+q
print(s.center(20,'*'))
print(s.partition('l'))
print("--"*20)

i='pkijk'
o='12345'
s='My name is priya'
t=s.maketrans(i,o)
v=s.translate(t)
print(v)
