#here name=KEY ABC=VALUE
a={'name':'ABC','roll':12}
print(a)
print(a['name'])
print(a['roll'])
print(a['name'][1])
print(a['name'][::-1])
print(a['name'][2:])
a['roll']=a['roll']-20
print(a)

'''
b={'course':'PYTHON','Marks':89}
print(b)
print(b['course'][::-1])
print(b['Marks'])
'''
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict.items(),key=lambda x:x[1])
print(sortedDict)
d=dict(sortedDict)
print(d)
