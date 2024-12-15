lt = []
print(lt)
print(type(lt))
lt = [44,34,22,55,44,23,66,"tree",7.88]
print(lt)
lt.append(100)
print(lt)

t1 = []
n = int(input("Enter array length:"))
for i in range(n):
    b = int(input("Enter array elements are:"))
    t1.append(b)

print(t1)

for i in range(n):
    print(t1[i],end=" ")
print()

for i in t1:
    print(i,end =" ")

