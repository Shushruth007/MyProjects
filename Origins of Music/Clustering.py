
import PCA
import numpy as np
import pandas as pd
import cartopy.crs as ccrs

import matplotlib.pyplot as plt
import mpl_toolkits


#Load Dataset
geomusT = pd.read_csv("FinalProj.csv").values
geomus = geomusT.T
geomus.shape


#Load componenst space
clusData = PCA.set_Proj()
print(clusData.shape)


#Load color list
color_list = ["#A93226", "#7D3C98", "#2471A3", "#17A589", "#229954", "#D4AC0D",
                "#BA4A00", "#2E4053", "#336915"]


#Set number of clusters
k = 8

# Assign k starpoints
C = clusData[np.random.randint(clusData.shape[0], size = k)]

for itr in range(40): # set number of k-mean iterations
    # initialize distance and cluster membership
    cluster_ind = np.zeros(len(clusData))
    distance = np.zeros((len(clusData), k))

    # find distance of every point to each centroid, and cluster membership
    i = 0
    centroid_calc = np.zeros((k, 3))
    for p in clusData:
        #find distance of points
        for d in range(k):
            distance[i][d] = (C[d][0] - p[0])**2 + (C[d][1] - p[1])**2



        #determine cluster membership
        for z in range(k):
            if (min(distance[i]) == distance[i][z]):
                cls_mem = z
                centroid_calc[z][0] += p[0]
                centroid_calc[z][1] += p[1]
                centroid_calc[z][2] += 1

        #update membership array
        cluster_ind[i] = cls_mem

        i += 1

    # update cluster centroids
    for i2 in range(k):
        C[i2][0] = centroid_calc[i2][0]/centroid_calc[i2][2]
        C[i2][1] = centroid_calc[i2][1]/centroid_calc[i2][2]


# Plot each iteration of k-means to show the first 4
i3 = 0
#Assign color to each cluster
for q in clusData:
    for n in range(k):
        if (cluster_ind[i3] == n):
            plt.plot(q[0],q[1], color= color_list[n] , marker='o')
    i3 += 1

#Plot Cluster
title = "Clusters with k = " + str(k)
plt.title(title)
plt.show()


#Load Location Data
spac_data = geomus[68:]
spac = spac_data.T


#Plot Component Space onto Map
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.scatter(spac_data[0], spac_data[1], zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Component space projected onto World Map')
plt.show()


#Plot CLusters on Maps
ax1 = plt.axes(projection=ccrs.PlateCarree())
ax1.stock_img()
i3 = 0
#Assign color to each cluster
for q in clusData:
    for n in range(k):
        if (cluster_ind[i3] == n):
            ax1.plot(spac[i3][0],spac[i3][1], color= color_list[n] , marker='o')
    i3 += 1

title2 = "Clusters projected onto World Map with k = " + str(k)
ax1.set_title(title2)
plt.show()







# In[ ]:
