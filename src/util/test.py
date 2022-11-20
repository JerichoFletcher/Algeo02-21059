import numpy as np
from eigenface import *

datasetVector = []
meanDataset = []
eigenFaceVector = []
arrRuangWajah = []

#m1 = np.array([[2,0,1], [1,2,0], [0,2,4]])
#m2 = np.array([[1,1,1], [0,1,0], [1,2,2]])
m1 = np.array([[1,1], [-2,-3]])
m2 = np.array([[1,-1], [3,2]])
m3 = np.array([[2,-2], [1,3]])
m4 = np.array([[1,2], [2,1]])
m5 = np.array([[1,3], [1,1]])

mdata = np.array([m1,m2,m3,m4,m5])
eigenface(mdata)

newM = np.array([[1,0], [3,2]])

idxmin = testImage(newM)
print(idxmin)

