#string formating
x='In the location'
print('Place.....here:',x)

print('place my variable here:%s'%x)

y=12.34
print('value:%s'%y)
print(type(y))

#floating formating
print('floating value:%1.2f'%(13.2554))
print('floating value:%0.2f'%(13.2554))

#convert to string
print('row convert to string :%r'%('abc\ndef'))
print('row convert to string :%s'%('abc\ndef'))
print('first:%s,second:%d,third:%0.2f'%('abc',3+4,3.344445))

print('first:%s,second:%s'%(2,2))
print('first:{x},second:{x}'.format(x='inserted'))
                                   
