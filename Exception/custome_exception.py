class priya(Exception):
    pass
def vote(a):
    if(a>=18):
        print('You are eligable for vote.')
    else:
        raise priya('You are not eligable for vote.')
    
a=int(input('Enter age: '))
try:
    vote(a)
except priya as e:
    print(e)
