import dataPreparation as dp
import random
import numpy as np
import matplotlib.pyplot as plt
import dataPreparation as dp
from matplotlib import style
from sklearn import neighbors
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




if __name__ == "__main__":
    result = add_st1_st2()
    dp.write_result("csvFiles/st1_st2_added.csv", result)
    fields = ['Result', 'ST1', 'ST2']
    dp.remove_fields("csvFiles/st1_st2_added.csv", "csvFiles/only_result_tp1_tp2.csv", fields)

    data = dp.get_csv_data("csvFiles/only_result_tp1_tp2.csv")
    del data[0]
    random.shuffle(data)
    train_count = 426 #70% of the dataset
    test_count = 183 #30% of the dataset

    train_data = data[:train_count]
    test_data = data[train_count:]

    train_x_data = []
    for i in range(len(train_data)):
        temp = []
        temp.append(train_data[i][1])
        temp.append(train_data[i][2])
        train_x_data.append(temp)

    test_x_data = []
    for i in range(len(test_data)):
        temp = []
        temp.append(test_data[i][1])
        temp.append(test_data[i][2])
        test_x_data.append(temp)


    train_y_data = [ row[0] for row in train_data ]
    test_y_data = [ row[0] for row in test_data ]

    knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    knn.fit(train_x_data, train_y_data)

    predictions = knn.predict(test_x_data)
    print(predictions)
    print(test_y_data)
    equals = 0
    nonEqual = 0
    for i in range(len(predictions)):
        if predictions[i] == test_y_data[i]:
            equals += 1
        else:
            nonEqual +=1

    print(equals)
    print(nonEqual)
    print("Accuracy:")
    accuracy = (float(equals)/float(len(predictions)))
    print(accuracy)

    




    #colors = ['r.', 'g.', 'b.', 'c.', 'k.', 'y.', 'm.']
    #for i in range (len(data)):
    #    plt.plot(int(data[i][1]),int(data[i][2]), colors[int(data[i][0])], markersize = 10)

    #plt.show()
