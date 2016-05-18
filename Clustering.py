import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys

#Read input file from user
file = open(sys.argv[2],"r")

#Read points from the input file
allx = []
ally = []
for line in file:
    line.replace("\n","")
    x,y = line.split(",")
    allx.append(float(x))
    ally.append(float(y))

point = []
for i in range(len(allx)):
    list=[allx[i],ally[i]]
    point.append(list)

#Save points to an array
X = np.array(point)
#Get the number of Clustering from user
n_clusters = int(sys.argv[1])
#Generate the Kmeans clustering
kmeans = KMeans(n_clusters)
kmeans.fit(X)
labels = kmeans.labels_
center = kmeans.cluster_centers_

#Generate random color by the number of clustering
colors = []
num = 0
while num < n_clusters:
    colors.append(np.random.rand(3))
    num+=1

#Generate the graph of clustering
for i in range(len(X)):
    #Get the label of each point
    label=labels[i]
    #Plot each point with different color depend on their label
    plt.scatter(X[i][0],X[i][1],c=colors[label])
    #Plot the center of clustering and reprensent it as *
    plt.scatter(center[label][0],center[label][1],marker="*",s=100)
    #Output the result in case the random color of two different clustering are too similar to be distinguished
    print('The center of ',X[i],'is',center[label],'and the label is ',label)
plt.show()