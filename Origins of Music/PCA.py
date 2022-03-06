#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


#Load Dataset
geomusT = pd.read_csv("FinalProj.csv").values
geomus = geomusT.T[0: 68]
m, n = geomus.shape
print(geomus.shape)


#Find mean of Data
geomusMean = geomus.mean(axis = 1)
print(geomusMean.shape)


#Center Data around mean
geomusMeanTileT = np.tile(geomusMean, (1058, 1))
geomusMeanTile = geomusMeanTileT.T
Z = geomus - geomusMeanTile


#Caluculate Covariance Matrix
C = np.matmul(Z,Z.T)/(n-1)

#Check shape
print(C.shape)


#Find components
D,V = np.linalg.eig(C)
idx = D.argsort()[::-1]
Vs = V[:,idx]

#Create component space
Proj = np.matmul(Vs[:,0:2].T,Z)
Proj.shape


#Plot component space
plt.plot(Proj[0], Proj[1], 'x')
plt.title("Component Space")
plt.show()


#Define function for Clustering script
def set_Proj():
    return Proj.T


# In[ ]:





# In[ ]:
