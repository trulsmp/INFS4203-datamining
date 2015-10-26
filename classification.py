import dataPreparation as dp
import random
import numpy as np
import matplotlib.pyplot as plt
import dataPreparation as dp
from matplotlib import style
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

style.use("ggplot")

def add_st1_st2():
    data = dp.get_csv_data("csvFiles/removedEmpty.csv")
    data[0].append('ST1')
    data[0].append('ST2')
    iterrows = iter(data)
    #Skip the header
    next(iterrows)
    for row in iterrows:
        row.append(int(row[1])-int(row[3]))
        row.append(int(row[2])+int(row[4]))
    return data

def knn(n_neighbors):
    #Get the data splitted in train and test, 70% and 30%
    train_x_data, train_y_data, test_x_data, test_y_data = makeTrainTestData()

    #Run the KNN classifier in sklearn
    knn = neighbors.KNeighborsClassifier(n_neighbors)

    knn.fit(train_x_data, train_y_data)

    predictions = knn.predict(test_x_data)
    #accuracy = get_accuracy(predictions,test_y_data)
    accuracy = accuracy_score(test_y_data, predictions)
    precision = precision_score(test_y_data, predictions)
    recall = recall_score(test_y_data, predictions)
    print("Results with n-neighbors: %d" %(n_neighbors))
    print("Accuracy:")
    print("%.3f" % accuracy)
    print("Precision:")
    print("%.3f" % precision)
    print("Recall:")
    print("%.3f" % recall)
    print("------------------------------------")


def naive_bayes():
    train_x_data, train_y_data, test_x_data, test_y_data = makeTrainTestData()
    clf = GaussianNB()
    clf.fit(train_x_data, train_y_data)
    predictions = clf.predict(test_x_data)
    accuracy = accuracy_score(test_y_data, predictions)
    precision = precision_score(test_y_data, predictions)
    recall = recall_score(test_y_data, predictions)
    print("Results for Naive Bayes:")
    print("Accuracy:")
    print("%.3f" % accuracy)
    print("Precision:")
    print("%.3f" % precision)
    print("Recall:")
    print("%.3f" % recall)
    print("------------------------------------")
    return 0

def makeTrainTestData():
    data = dp.get_csv_data("csvFiles/only_result_tp1_tp2.csv")
    #delete header
    del data[0]
    random.shuffle(data)
    train_count = 426 #70% of the dataset
    test_count = 183 #30% of the dataset

    train_data = data[:train_count]
    test_data = data[train_count:]

    #Filter out the data and results into train and test
    train_x_data = []
    for i in range(len(train_data)):
        temp = []
        temp.append(int(train_data[i][1]))
        temp.append(int(train_data[i][2]))
        train_x_data.append(temp)

    test_x_data = []
    for i in range(len(test_data)):
        temp = []
        temp.append(int(test_data[i][1]))
        temp.append(int(test_data[i][2]))
        test_x_data.append(temp)

    #Get the results of the matches
    train_y_data = [int(row[0]) for row in train_data]
    test_y_data = [int(row[0]) for row in test_data]

    return train_x_data, train_y_data, test_x_data, test_y_data

if __name__ == "__main__":
    result = add_st1_st2()
    dp.write_result("csvFiles/st1_st2_added.csv", result)
    fields = ['Result', 'ST1', 'ST2']
    dp.remove_fields("csvFiles/st1_st2_added.csv", "csvFiles/only_result_tp1_tp2.csv", fields)
    knn(10)
    naive_bayes()



    #colors = ['r.', 'g.', 'b.', 'c.', 'k.', 'y.', 'm.']
    #for i in range (len(data)):
    #    plt.plot(int(data[i][1]),int(data[i][2]), colors[int(data[i][0])], markersize = 10)

    #plt.show()
