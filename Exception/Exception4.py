print('Hello')
print('Hello')
print('Hello')
print('Hello')
a=int(input('Enter a no.'))
b=int(input('Enter a no.'))
class A:
    def show(self):
        print('Hello show')
ob=None
c='kolkata'
lt=[1,2,3,4,5,6]
try:
    print(a/b)
    print(lt[7])
    print(c[8])
    ob.show()
except ZeroDivisionError as e:
    print(e)
except AttributeError as e:
    print(e)
except IndexError as e:
    print(e)
print('Hello')
print('Hello')
print('Hello')
