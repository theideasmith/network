import pandas as pd
import numpy as np
import pprint
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel('./CElegansNeuronTables.xls',sheet_name="Connectome")

M = df.as_matrix()
# Getting Edge As
A = M[:,0]
# Getting Edge Bs
B = M[:,1]

graph = nx.DiGraph()

# Collects data for node_peers and node_index
for c in xrange(0,len(A)):
    graph.add_node(A[c])
    graph.add_node(B[c])
    graph.add_edge(A[c],B[c])
nx.write_graphml(graph, './nematode-connectome.graphml')
