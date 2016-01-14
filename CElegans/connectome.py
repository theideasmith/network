import matplotlib.pyplot as plt
import networkx as nx
import connectome_load as loader

graph = loader.as_graph()
edge_colors = loader.colored_edges()

plt.figure(figsize=(20,10))
nx.draw_graphviz(graph, "dot", edge_color=edge_colors, node_size=5)
plt.show()


# Remove the GJs from the gapjunctions.
