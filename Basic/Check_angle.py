a=int(input('Enter 1st angle:'))
b=int(input('Enter 2nd angle:'))
c=int(input('Enter 3rd angle:'))
if(a+b+c==180):
    #print('The triangle is formed.')
    if(a<90 and b<90 and c<90):
        print('The triangle is acute angled triangle')
    elif(a>90 or b>90 or c>90):
        print('The triangle is obtuse angled triangle')
    elif(a==90 or b==90 or c==90):
        print('The triangle is right angled triangle')
else:
    print('The triangle is not formed.')
