'''
---===---===---===---===---===---===---===
  An Assortment of Connectivity Functions
        for Generating Networks

Akiva Lipshitz
November 2015
===---===---===---===---===---===---===---
'''

''' The generator for an n-edged polygon generator '''
def npoly(l):
    return lambda i,n: (n==1 or n==(l-1))

''' Whether n is in a given range'''
def __inclusive_range_checker( start, n, stop):
    return ((n>=start) and (n<=stop))


''' The generator for a network
    in which node i is connected to all node z's
    where:
        z = f(i)
        i<z<n
'''
def max_range_function(f):
    return lambda i,n: __inclusive_range_checker(i+1,n,f(i))


''' The generator for a network
    in which node i is connected to node z
    where:
        z = x*i
        i<z<n
'''
def range_product(x):
    return max_range_function(lambda i:i*x)
