import shutil
import os
import math as m

# Clear the cache
shutil.rmtree('./shapes')
os.mkdir('./shapes')

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import matplotlib.pyplot as plt
import networkx as nx
import networkgen as ng



for j in xrange(1,50):
	# The graph generator function, Z
	range = ng.DirectedGenerators.range_product(2)
	Z = lambda i,n: range(i,n) or n==1

	# Generate adjacency matrix of j nodes, using generator Z
	matrix = ng.matrix_linear(Z,j)

	# Generate graph G from adjacency matrix
	G=nx.from_numpy_matrix(matrix)

	# Draw the graph
	pos=nx.spring_layout(G)
	nx.draw(G, pos, node_color="#A0CBE2", width=4, )
	# plt.show()
	# Save the rendered graph
	plt.savefig("./shapes/shape{0}.png".format(j),format="PNG")

	# Reset rendering buffer
	plt.clf()
