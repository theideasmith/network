import networkx as nx
import pandas as pd
import numpy as np
connectome = pd.read_excel('./CElegansNeuronTables.xls',sheet_name="Connectome").as_matrix()

# Getting Edge As
A = connectome[:,0]
# Getting Edge Bs
B = connectome[:,1]

connection_types = connectome[:,2]
num_connections = connectome[:,3]
neurotransmitter_types = connectome[:,4]

def _populate_graph(g):
    # Collects data for node_peers and node_index
    for c in xrange(0,len(A)):
        if not g.has_edge(A[c],B[c]):
            # edge_colors.append(colormap[neurotransmitter_types[c]])
            g.add_edge(A[c],
                        B[c],
                       connection_type=connection_types[c],
                       neurotransmitter=neurotransmitter_types[c])


def as_graph():
    graph = nx.Graph()
    graph.add_nodes_from(
        np.unique(
            np.concatenate((A,B))
        )
    )
    _populate_graph(graph)

    return graph

def as_digraph():
    graph = nx.DiGraph()
    graph.add_nodes_from(
        np.unique(
            np.concatenate((A,B))
        )
    )
    _populate_graph(graph)
    return graph

GRAPH = as_graph()
DIGRAPH = as_digraph()
NEUROTRANSMITTERS = [
 u'Acetylcholine',
 u'Acetylcholine_GJ',
 u'Acetylcholine_Tyramine',
 u'Acetylcholine_Tyramine_GJ',
 u'Dopamine',
 u'Dopamine_GJ',
 u'FMRFamide',
 u'FMRFamide_GJ',
 u'FRMFemide',
 u'FRMFemide_GJ',
 u'GABA',
 u'GABA_GJ',
 u'Glutamate',
 u'Glutamate_GJ',
 u'Octapamine',
 u'Octapamine_GJ',
 u'Serotonin',
 u'Serotonin_Acetylcholine',
 u'Serotonin_Acetylcholine_GJ',
 u'Serotonin_GJ',
 u'Serotonin_Glutamate',
 u'Serotonin_Glutamate_GJ'
]

def colored_edges():
    graph = as_graph()

    colorbase =256/len(NEUROTRANSMITTERS)
    colormap_neurotrans = { NEUROTRANSMITTERS[i]: colorbase*(i) for i in range(0, len(NEUROTRANSMITTERS))}

    edge_colors = []

    # Collects data for node_peers and node_index
    for c in xrange(0,len(A)):
        if not graph.has_edge(A[c],B[c]):
            edge_colors.append(colormap_connection_type[connection_types[c]])

    return edge_colors
