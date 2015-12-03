import time
import shutil
import os
import math as m

# Clear the cache
shutil.rmtree('./shapes')
os.mkdir('./shapes')

import matplotlib.pyplot as plt
import networkx as nx
import networkgen as ng
import generators as gen

plt.ion()

for j in xrange(1,50):
	# The graph generator function, Z
	range = gen.range_product(2)
	Z = lambda i,n: range(i,n) or n==1

	# Z = lambda i,n: (i%2==0) or n==1
	# Generate adjacency matrix of j nodes, using generator Z
	matrix = ng.matrix_circular(j,Z)

	# Generate graph G from adjacency matrix
	G=nx.from_numpy_matrix(matrix)

	# Draw the graph
	pos=nx.spring_layout(G)
	plt.clf()
	nx.draw(G,pos, node_color="#A0CBE2", width=4)
	# time.sleep(1)
	# plt.plot()
	plt.savefig("./shapes/shape{0}.png".format(j),format="PNG")

# Z = lambda i,n: 1
# matrix = ng.matrix_circular(80, dg.DirectedGenerators.npoly(80))
#
# G=nx.from_numpy_matrix(matrix)
#
# degree_sequence=sorted(
#     nx.degree(G).values(),
#     reverse=True) # degree sequence
#
# print degree_sequence
# #print "Degree sequence", degree_sequence
# dmax=max(degree_sequence)
#
# plt.loglog(degree_sequence,'b-',marker='o')
# plt.title("Degree rank plot")
# plt.ylabel("degree")
# plt.xlabel("rank")
#
# # draw graph in inset
# plt.axes([0.45,0.45,0.45,0.45])
# Gcc=sorted(
#       nx.connected_component_subgraphs(G)
#     , key = len
#     , reverse=True)[0]
#
# pos=nx.spring_layout(Gcc)
# plt.axis('off')
# nx.draw_networkx_nodes(Gcc,pos,node_size=20)
# nx.draw_networkx_edges(Gcc,pos,alpha=0.4)
#
# plt.savefig("degree_histogram.png")
# plt.show()
