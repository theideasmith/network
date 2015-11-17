import numpy as np

def __foundation_matrix(num_nodes): 
    a = np.arange(num_nodes).reshape([1,num_nodes])
    b = np.transpose(a)
    return (b,a)

def matrix_circular(z, num_nodes): 
    a,b=__foundation_matrix(num_nodes)
    Z=np.vectorize(lambda i,j: z(i, (j+1)%(i+1)))
    return Z(a,b)

def matrix_linear(z, num_nodes):
    a, b = __foundation_matrix(num_nodes)
    # Vectorize generator z
    Z = np.vectorize(lambda i,j: z(i, j-i))
    return Z(a,b)

''' For directed graphs '''
class DirectedGenerators:
    ''' The generator for an n-edged polygon generator '''
    @classmethod
    def npoly(cls, l):
        return lambda i,n: (n==1 or n==(l-1))

    ''' Whether n is in a given range'''
    @classmethod
    def __inclusive_range_checker(cls, start, n, stop):
        return ((n>=start) and (n<=stop))


    ''' The generator for a network
        in which node i is connected to all node z's
        where:
            z = f(i)
            i<z<n
    '''
    @classmethod
    def max_range_function(cls,f):
        return lambda i,n: cls.__inclusive_range_checker(i+1,n,f(i))


    ''' The generator for a network
        in which node i is connected to node z
        where:
            z = x*i
            i<z<n
    '''
    @classmethod
    def range_product(cls,x):
        return cls.max_range_function(lambda i:i*x)
