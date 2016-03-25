import transform as tf
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

wd = tf.wormData[tf.wormData.keys()[0]]
sklearn_pca = PCA(wd['deltaFOverF_deriv'])
sklearn_pca = PCA(n_components=3)

transf = sklearn_pca.fit_transform(wd['deltaFOverF_deriv'])
#cov = sklearn_pca.get_covariance()
backtransformed = sklearn_pca.inverse_transform(transf)

components = sklearn_pca.components_

c302_loc = "."

# 303 elements, first is removed and saved as time steps (seconds)
# demo_data.dat is a proper c302 output .dat file
c302 = np.loadtxt(c302_loc + '/demo_data.dat')
c302_time = c302[:,0]
data = np.delete(c302, 0, 1)

c302_deriv = np.diff(c302.T).T

# PCA on simulation data
c302_pca, c302_trans = tf.scikit_pca(data, 3)

c302_neurons = tf.c302_list(c302_loc + "/LEMS_c302_C_Full.xml")


#plot simulation results
def plot_c302_result():
  fig = plt.figure(figsize=(10,20))
  gs  = gridspec.GridSpec(1,1)
  subplot1 = fig.add_subplot(gs[0,0])
  subplot1.set_title("c302 simulation")
  subplot1.pcolor(data.T)
  subplot1.axis('tight')

  fig.show()


plot_c302_result()

