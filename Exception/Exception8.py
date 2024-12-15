a=int(input('Enter number '))

try:
    if(a>0):
        print('This is positive no.')
        try:
            if(a%2==0):
                print('This is even.')
            else:
                raise ValueError('This is odd no.')
        except Exception as e:
            print(e)
    else:
        raise ValueError('This is not positive no.')
    
except Exception as e:
    print(e)
    
            
