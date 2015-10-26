clusters = 2
import numpy as np
import matplotlib.pyplot as plt
import dataPreparation as dp
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering


def getCentroid(X, labels):
    cl1xSum = 0
    cl1ySum = 0
    cl2xSum = 0
    cl2ySum = 0
    cl1Number = 0
    cl2Number = 0
    #SUM of the values in each cluster
    for i in range(len(X)):
        if (labels[i] == 0):
            cl1Number += 1
            cl1xSum += X[i][0]
            cl1ySum += X[i][1]
        else:
            cl2Number += 1
            cl2xSum += X[i][0]
            cl2ySum += X[i][1]

    #Find the average X and Y point for each cluster
    Cl1xCentroidPoint = cl1xSum/cl1Number
    Cl1yCentroidPoint = cl1ySum/cl1Number

    Cl2xCentroidPoint = cl2xSum/cl2Number
    Cl2yCentroidPoint = cl2ySum/cl2Number

    #Print the points for visual
    print("Cl2 numbers")
    print("Cluster 1 Centroids")

    print(Cl1xCentroidPoint, Cl1yCentroidPoint)

    print("Cluster 2 Centroids")
    print(Cl2xCentroidPoint, Cl2yCentroidPoint)

    #Combine the x,y centroid points in a list and return it
    centroids = [Cl1xCentroidPoint, Cl1yCentroidPoint, Cl2xCentroidPoint, Cl2yCentroidPoint]
    return centroids


def calculate_SSE(centroids, X, labels):
    SSEsumCl1 = 0
    SSEsumCl2 = 0
    #Find SSE according to formula
    for i in range(len(X)):
        if labels[i] == 0:
            xd = centroids[0]-X[i][0]
            yd = centroids[1]-X[i][1]
            distance = xd*xd + yd*yd
            SSEsumCl1 += distance
        else:
            xd = centroids[2]-X[i][0]
            yd = centroids[3]-X[i][1]
            distance = xd*xd + yd*yd
            SSEsumCl1 += distance
    return(SSEsumCl1+SSEsumCl2)


def K_means(colors, X):
    #Perform the clustering using K-means
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)

    #Get the cluster labels and centroids
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    #Find the SSE
    centroid2 = getCentroid(X, labels)
    SSEK = calculate_SSE(centroid2, X, labels)

    #Plot the points and the centroids to visualize
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

    titleString = "K-means clustering with SSE = "
    titleString += str(SSEK)
    plt.title(titleString)
    plt.xlabel("ACE: Number of aces in match")
    plt.ylabel("TPW: Total Points won in match")

    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=5, zorder=10)
    plt.show()


#Hierical
def hierical(colors, X):
    #Perform the clustering using ward hierical algorithm
    ms = AgglomerativeClustering(linkage='ward', n_clusters=2)
    ms.fit(X)

    #Get the cluster labels and centroids
    labels = ms.labels_
    centroids = getCentroid(X, labels)

    #Find the SSE
    SSEH = calculate_SSE(centroids, X, labels)

    #Plot the points and the centroids to visualize
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

    titleString = "Hierarchical clustering with SSE = "
    titleString += str(SSEH)
    plt.title(titleString)
    plt.xlabel("ACE: Number of aces in match")
    plt.ylabel("TPW: Total Points won in match")

    xCentroid = [centroids[0], centroids[2]]
    yCentroid = [centroids[1], centroids[3]]
    plt.scatter(xCentroid, yCentroid, marker='x', s=150, linewidths=5, zorder=10)

    plt.show()

    #plot with gender as colors
    gender_labels = dp.get_csv_data("csvFiles/only_gender.csv")

    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[int(gender_labels[i+1][0])], markersize=10)

    plt.title("Point colour based on gender, Green: Women, Red: Men")
    plt.xlabel("ACE: Number of aces in match")
    plt.ylabel("TPW: Total Points won in match")

    xCentroid = [centroids[0], centroids[2]]
    yCentroid = [centroids[1], centroids[3]]
    plt.scatter(xCentroid, yCentroid, marker='x', s=150, linewidths=5, zorder=10)

    plt.show()


def add_ace_tpw():
    data = dp.get_csv_data("csvFiles/removedEmpty.csv")
    data[0].append('ACE')
    data[0].append('TPW')
    iterrows = iter(data)
    #Skip the header
    next(iterrows)
    for row in iterrows:
        row.append(int(row[5])+int(row[6]))
        row.append(int(row[7])+int(row[8]))
    return data


if __name__ == "__main__":
    result = add_ace_tpw()
    dp.write_result("csvFiles/ace_tpw_added.csv", result)
    fields = ['ACE', 'TPW']
    dp.remove_fields("csvFiles/ace_tpw_added.csv", "csvFiles/only_ace_tpw.csv", fields)
    fields = ['Gender']
    dp.remove_fields("csvFiles/removedEmpty.csv", "csvFiles/only_gender.csv", fields)

    #Datapoints from csv file, skip header
    X = np.genfromtxt("csvFiles/only_ace_tpw.csv", dtype=int, delimiter=',', skip_header=1)
    colors = 10*['r.', 'g.', 'b.', 'c.', 'k.', 'y.', 'm.']

    K_means(colors, X)
    hierical(colors, X)
