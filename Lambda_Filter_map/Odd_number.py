odd=lambda a:(a%2!=0)
a=[1,2,3,4,5,6,7,8]
lt=filter(odd,a)
for i in lt:
    print(i,end=' ')
