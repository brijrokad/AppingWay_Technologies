L1 = ['a','b','c']
L2 = ['b','d']

def intersection(L1,L2):
    return list(set(L1) & set(L2))
## intersection() is a operator which returns the common element of two sets
print ("Common Elements in list L1 and L2:",intersection(L1,L2))

x = list(set(L1) - set(L2))
print ("Elements which are in list L1 but not in list L2:",x)
## here two sets will be compared and if elements are found common, then they
## will be removed from the set L1 and remaining  elements wil be returned