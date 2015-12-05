from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import csv

my_data = genfromtxt('data.csv', delimiter=',')

points1X = my_data[:,0]
points1Y = my_data[:,1]
points1Z = my_data[:,2]

points1X = np.reshape(points1X,points1X.size)
points1Y = np.reshape(points1Y,points1Y.size)
points1Z = np.reshape(points1Z,points1Z.size)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(points1X, points1Y, points1Z, 'd', markersize=8, markerfacecolor='red', label='points1')
plt.show()

