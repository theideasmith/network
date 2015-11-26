import numpy as np
import directedgenerators

def __foundation_matrix(num_nodes):
    a = np.arange(num_nodes).reshape([1,num_nodes])
    b = np.transpose(a)
    return (b,a)

def __spawn_matrix(
    num_nodes,
    matrix_generator,
    connection_generator):


    a,b=__foundation_matrix(num_nodes)
    C = matrix_generator

    '''
    First get the value for i,j of the network generator ma-
    trix, and then get the weight of the connection between
    N_i and N_{i+n}
    '''

    Z=np.vectorize(
        lambda i,j: connection_generator(i,
                        matrix_generator(i,j)
                    )
    )
    return Z(a,b)


'''
Given graph G and associated adjacency matrix M

    [[ 1 2 3 0 ]
M =  [ 1 2 3 0 ]
     [ 1 2 3 0 ]
     [ 1 2 3 0 ]]

    [[ 0 1 2 3 ]
C(M) = [ 3 0 1 2 ]
     [ 2 3 0 1 ]
     [ 1 2 3 0 ]]

C(i,j) = (n-i+j)%n, where i is the row and j the column of
the adjacency matrix M for graph G, and n is the total numb-
er of nodes in N(G)(vertices of g)

This makes the graph forward facing circular.
'''

def matrix_circular(num_nodes, z):

    C = lambda i,j: (num_nodes-i+j)%num_nodes

    return __spawn_matrix(num_nodes, C, z)

def matrix_linear(num_nodes, z):

    C = lambda i,j: j-i

    return __spawn_matrix(num_nodes, C, z)
