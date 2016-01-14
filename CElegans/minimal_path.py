import numpy as np
import pandas as pd
import networkx as nx
import matplotlib as mpl

def minimalpath(innode, outnode):
  print("Code here");


connectome = pd.read_excel('./OurCElegansNeuronTables.xls',sheet_name="Connectome").as_matrix()
neuronmuscle = pd.read_excel('./OurCElegansNeuronTables.xls',sheet_name="NeuronsToMuscle").as_matrix()
sensory = pd.read_excel('./OurCElegansNeuronTables.xls',sheet_name="Sensory").as_matrix()



A = connectome[:,0]
B = connectome[:,1]

connection_types = connectome[:,2]
num_connections = connectome[:,3]
neurotransmitter_types = connectome[:,4]

muscleneuron = neuronmuscle[:,1]
muscletarget = neuronmuscle[:,2]
muscleconnections = neuronmuscle[:,3]
muscleneurotransmitter = neuronmuscle[:,4]

sensoryneuron = sensory[:,1]



alldata = np.concatenate((A,B))
nodes = np.unique(alldata)

outputs = np.unique(muscleneuron)
inputs = np.unique(sensoryneuron)

print (nodes)
print (len(nodes))
print (len(A))


graph = nx.MultiDiGraph()

graph.add_nodes_from(nodes)

neurotransmitters = np.unique(neurotransmitter_types)

#drawing_colors = []

# Collects data for node_peers and node_index
#for c in xrange(0,len(nodes)):
#  graph.add_node(nodes[c])


for c in xrange(0, len(A)):
#  if neurotransmitter_types[c] == "Glutamate":
    if connection_types[c] != "GapJunction":
      graph.add_edge(A[c],
                 B[c],
                 weight=num_connections[c],
                 key=0,
                 connectiontype=connection_types[c],
                 neurotransmitter=neurotransmitter_types[c])
    else:
      graph.add_edge(A[c],
                 B[c],
                 weight=400,
                 key=1,
                 connectiontype=connection_types[c],
                 neurotransmitter=neurotransmitter_types[c])

pos = nx.random_layout(graph)
print(pos)

nx.draw(graph)
nx.readwrite.write_graphml(graph,'./out.xml',encoding='utf-8',prettyprint=True)
