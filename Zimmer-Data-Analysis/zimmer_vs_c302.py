import numpy as np
import matplotlib.pyplot as plt
import transform as tf

c302_loc = './CElegansNeuroML/CElegans/pythonScripts/c302'

zimmer = tf.wormData[tf.wormData.keys()[0]]
#Because this is necessary to have neuron*data
c302 = np.loadtxt(c302_loc + '/c302_A_Full.dat').T * 1000 #Convert from s to ms




