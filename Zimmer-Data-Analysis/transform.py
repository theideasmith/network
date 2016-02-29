import matplotlib.pyplot as plt
from matplotlib import gridspec
import scipy.io as scio
import os
import sklearn.decomposition as deco
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import numpy as np

MAT_EXTENSION = '.mat'

def extract_nids_list(wormdata):
    nids = wormdata['NeuronIds'].transpose()
    total = []
    for x in nids:
        for j in x:
            for y in j:
                d = []
                if len(y)==0: total.append(None)
                else:
                    for n in y:
                        listed = n.tolist()
                        if len(listed)>0: d.append(listed[0] )
                    total.append(d)
    return total

def extract_matfile(fname):
    try:
        matfile = scio.loadmat(fname)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        raise
    data=matfile['wbData'][0][0]

    keyed_data = { data.dtype.names[i]: data[i] for i in range(len(data.dtype.names))}
    keyed_data['NeuronIds']  = extract_nids_list(keyed_data)
    return keyed_data

def loadfiles(files):
    datasets = { file: extract_matfile('wbdata/'+ file) for file in files if os.path.splitext(file)[1] == MAT_EXTENSION}
    return datasets

def graph_worm_overview(wormdata):


    fields = ['deltaFOverF_deriv',
              'deltaFOverF_bc',
              'tv',
              'NeuronIds',
              'FlNm',
              'deltaFOverF']

    if wormdata.keys() != fields:
        raise TypeError("Passed wormdata lacks necessary fields")

    fig = plt.figure(figsize=(10,20))

    gs  = gridspec.GridSpec(3,1)

    deriv_ax = fig.add_subplot(gs[0,0])
    deriv_ax.set_title("Fluorescence Derivative")
    deriv_ax.pcolor(wormdata['deltaFOverF_deriv'].T)
    deriv_ax.axis('tight')

    bc_ax = fig.add_subplot(gs[1,0])
    bc_ax.set_title("Fluorescence Bleach Cancelled")
    bc_ax.pcolor(wormdata['deltaFOverF_bc'].T)
    bc_ax.axis('tight')

    f_over_f = fig.add_subplot(gs[2,0])
    f_over_f.set_title("Fluorescence Raw")
    f_over_f.pcolor(wormdata['deltaFOverF'].T)
    f_over_f.axis('tight')

    fig.tight_layout()

    return fig

def draw_worm_overview_graphs(data):
    for flnm,worm in data.iteritems():
        file = os.path.splitext(flnm)[0] + '.png'
        graph_worm_overview(worm).savefig(file, bbox_inches="tight")

wormData = loadfiles(os.listdir('./wbdata'))

from mpl_toolkits.mplot3d import Axes3D



from matplotlib import cm

def plot_manifolds():

    def get_dims(n):
        # Minimizes the dimensions of a grid (xy) to plot n elements
        import math
        s = math.sqrt(float(n))
        x = int(math.ceil(s))
        y = int(math.floor(s))
        return (x,y)

    def dims_coord(dims, n):
        x,y = dims
        a = n/y
        b = n%(y)
        return (a,b)

    def scikit_pca(X):

        # PCA
        sklearn_pca = PCA(n_components=3)
        X_transf = sklearn_pca.fit_transform(X)
        return X_transf

    dims = get_dims(5)
    fig = plt.figure(figsize=(20,10))
    gs  = gridspec.GridSpec(3,2)
    i = 0
    for k,v in wormData.iteritems():
        x,y = dims_coord(dims, i)
        pca = scikit_pca(v['deltaFOverF_deriv'])

        ax = fig.add_subplot(gs[x,y], projection="3d")
        print "-"*30
        print pca
        ax.plot(pca[:,0], pca[:,1], pca[:,2])
        ax.set_title('PCA on fluorescence derivative')

        i+=1

    return fig


    return total




def c302_list(file):
    from lxml import etree
    xml = etree.parse(file)
    columns = xml.findall('.//OutputColumn')
    return map(lambda c: c.values()[0], columns)



