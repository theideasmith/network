
import matplotlib.pyplot as plt
import networkx as nx
import csv
import os

import numpy as np

CSV_PATH = "./data/random-generated-graph-data.csv"
IMG_PATH = "./data/random-generated-graph-img/"


'''
============================================================
Based on chapter 1 of the paper
		Characterization of Complex Networks:
			  A Survey of measurements
============================================================

'''

def safe_path_relative(save_path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), save_path)
    # if(not os.path.exists(path)):
    #     raise Exception("Given path {0} is not a directory".format(save_path))

    return path

def csv_writer(name=CSV_PATH):
    path = safe_path_relative(name)

    csv_binary = open(path, "wb")
    writer = csv.writer(csv_binary, delimiter=',', quotechar='\'', quoting=csv.QUOTE_NONE)
    return writer

def savegraph(G, pos, save_path):
    path=safe_path_relative(save_path)
    plt.clf()
    nx.draw(G,pos, node_color="#A0CBE2", width=4)
    plt.savefig(path.format(save_path),format="PNG")

def save_csv(data, header, writer):
    writer.writerow(header)
    writer.writerows(data)


# Incides in Matrix
N = 0
P = 1
AVG_CLUSTERING   = 1

def graph_collect(n, p, G):
    data =  [
        n, p,
        nx.average_clustering(G)
    ]
    return data

def data_pairs(array, index1, index2):
    return [[array[j][index1],array[j][index2]] for j in xrange(0,len(array))]

def collect_data():

    A = [
      graph_collect(n, 0.1*p, nx.fast_gnp_random_graph(n,0.1*p))
      for n in xrange(1,51)
      for p in xrange(1,11)
    ]

    return A

def reshape_data(A):
    M = np.array(A)
    return M.reshape((50,10,M.shape[1]))

def extract_dimensions(B):
    x = B[:,:,0]

    y = B[:,:,1]

    z = B[:,:,2]
    return (x,y,z)
