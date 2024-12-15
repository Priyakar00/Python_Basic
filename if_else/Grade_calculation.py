a=int(input('Enter 1st marks:'))
b=int(input('Enter 2nd marks:'))
c=int(input('Enter 3rd marks:'))
d=int(input('Enter 4th marks:'))
e=int(input('Enter 5th marks:'))
total=a+b+c+d+e
print('Total marks:',total)
avg=total/5
print('Average marke:',avg)

if(avg>=90):
    print('Grade AA')
elif(avg>=80):
        print('Grade A+')
elif(avg>=70):
        print('Grade A')
elif(avg>=60):
        print('Grade B+')
elif(avg>=50):
        print('Grade B')
elif(avg>=40):
        print('Grade C')
else:
    print('Grade D')
