#using HRHA calculate power
def power(base,exp):
    p=1
    for i in range(1,exp+1):
        p=p*base
    return p

'''    
y=power(2,3)
print(y)
'''
