# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    T = []
    E = []
    Y = []
    U = []
    P = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    Young = 1
    Presbyopic = 2
    Prepresbyopic = 3
    Myope = 1
    Hypermetrope = 2
    No = 1
    Yes = 2
    Normal = 1
    Reduced = 2

    E = [[1, 1, 2, 1], [1, 2, 2, 1], [1, 1, 2, 1], [3, 1, 2, 1], [3, 2, 1, 2], [3, 2, 2, 1], [2, 1, 2, 1], [2, 2, 2, 1]]

    T = [[1, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 1], [1, 2, 1, 2], [1, 2, 1, 1], [3, 1, 1, 1], [3, 2, 2, 1], [2, 1, 1, 1],
         [2, 1, 2, 1], [2, 2, 1, 2], [2, 2, 1, 1], [2, 2, 2, 1]]

    X = [[1, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 2], [1, 1, 2, 1], [1, 2, 1, 2], [1, 2, 1, 1], [1, 2, 2, 2], [1, 2, 2, 1],
         [2, 1, 1, 2], [2, 1, 1, 1], [2, 1, 2, 2], [2, 1, 2, 1], [2, 2, 1, 2], [2, 2, 1, 1], [2, 2, 2, 2], [2, 2, 2, 1],
         [3, 1, 1, 2], [3, 1, 1, 1], [3, 1, 2, 2], [3, 1, 2, 1], [3, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 2], [3, 2, 2, 1]]

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    Yes = 1
    No = 2

    P = [1, 1, 1, 1, 2, 2, 1, 2]
    U = [2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2]
    Y = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2]

    # loop your training and test tasks 10 times here
for i in range(10):

    # fitting the decision tree to the data setting max_depth=3
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
    clf = clf.fit(T, U)

    # read the test data and add this data to dbTest
    # --> add your Python code here
    dataTest = ['contact_lens_test.csv']

    for dm in dataTest:

        dbTest = []

        # reading test data in a csv file
        with open(dm, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)
    correct = 0
    accuracy = 0
    accuracyArray = []
    k = 0
    j = 0
    for data in dbTest:
        # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
        # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        # --> add your Python code here

        class_predicted = clf.predict([[1, 1, 1, 1]])[0]
        class_predicted2 = clf.predict([[1, 2, 1, 1]])[0]
        class_predicted3 = clf.predict([[1, 1, 1, 2]])[0]
        class_predicted4 = clf.predict([[2, 2, 1, 2]])[0]
        class_predicted5 = clf.predict([[2, 1, 1, 1]])[0]
        class_predicted6 = clf.predict([[2, 1, 2, 2]])[0]
        class_predicted7 = clf.predict([[3, 1, 2, 1]])[0]
        class_predicted8 = clf.predict([[3, 1, 1, 2]])[0]

        # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        # --> add your Python code here

        classify = [class_predicted, class_predicted2, class_predicted3, class_predicted4, class_predicted5,
                    class_predicted6, class_predicted7, class_predicted8]

        if int(classify[j]) == 1 and data[4] == 'Yes' or int(classify[j]) == 2 and data[4] == 'No':
            correct += 1
        j += 1

    # find the lowest accuracy of this model during the 10 runs (training and test set)
    # --> add your Python code here

    accuracy = correct / 8
    accuracyArray.append(accuracy)

# lowest1 = min(accuracyArray)
lowest2 = min(accuracyArray)
# lowest3 = min(accuracyArray)

# print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
# your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
# --> add your Python code here

# print("contact_lens_training_1.csv: " + str(lowest1)) #accuracy = .5
print("contact_lens_training_2.csv: " + str(lowest2))  # accuracy = .75
# print("contact_lens_training_3.csv: " + str(lowest3))  # accuracy = .875
