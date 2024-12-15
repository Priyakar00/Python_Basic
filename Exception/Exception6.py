def vote(a):
    if(a>=18):
        print('You are eligable for vote.')
    else:
        raise ValueError('You are not eligable for vote.')
    
a=int(input('Enter age: '))
try:
    vote(a)
except Exception as e:
    print(e)
