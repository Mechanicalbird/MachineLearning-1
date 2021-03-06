import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

#plt.scatter(X[:,0], X[:,1], s=150)
#plt.show()

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors= ["g.","r.", "c.","b.","k.","o."]


class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
       delf.k = k
       self.tol = tol
       self.max_iter = max_iter

    def fot(self,data)
       
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in X:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)


            for classification in self.classifications:
                pass
                #self.centroids[classification] = np.average(self.classifications[classification], axis = 0)
                


    def predict(self,data)
       pass















