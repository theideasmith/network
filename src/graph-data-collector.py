
import networkx as nx
import csv

'''

Based on chapter 1 of the paper Characterization of Complex Networks:
A Survey of measurements, which is located file:///Users/akivalipshitz/Dropbox/Life/Tenth/Computational%20Neuroscience/Papers/Network-Characterization.pdf

List of relevant cited articles in this one:

Percolation and Random Graphs: 1, 2,3,4, 5,6,7
Watts and Strogatz small world: 8
Brabasi and Albert scale free: 9
Girvan and Newman on Community Structure: 10

Structure and Dynamics of Complex Networks: 21, 23


The goal of this micro project is to study the relationship between different graph properties. It will generate the necessary data and run the necessary analysis to cluster graphs based connectivity, average path length, and degree distribution.




Graph properties:

N(G): Set of vertices of graph G
E(G): Set of edges of graph G
D(n): degree of node n
