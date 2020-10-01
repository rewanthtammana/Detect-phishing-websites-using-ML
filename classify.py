from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from utils import generate_data_set

import numpy as np
import sys

def load_data():
    '''
    Load data from CSV file
    '''
    # Load the training data from the CSV file
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int32)

    # Extract the inputs from the training data
    inputs = training_data[:,:-1]

    # Extract the outputs from the training data
    outputs = training_data[:, -1]

    # This model follow 80-20 rule on dataset
    # Split 80% for traning and 20% testing
    boundary = int(0.8*len(inputs))

    training_inputs, training_outputs, testing_inputs, testing_outputs = train_test_split(inputs, outputs, test_size=0.33)

    # Return the four arrays
    return training_inputs, training_outputs, testing_inputs, testing_outputs

def run(classifier, name):
    '''
    Run the classifier to calculate the accuracy score
    '''
    # Load the training data
    train_inputs, test_inputs,train_outputs, test_outputs = load_data()

    # Train the decision tree classifier
    classifier.fit(train_inputs, train_outputs)

    # Use the trained classifier to make predictions on the test data
    predictions = classifier.predict(test_inputs)

    # Print the accuracy (percentage of phishing websites correctly predicted)
    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    print "Accuracy score using {} is: {}\n".format(name, accuracy)


if __name__ == '__main__':
    '''
    Main function -
    Following are several models trained to detect phishing webstes.
    Only the best and worst classifier outputs are displayed.
    '''

    # Decision tree
    # classifier = tree.DecisionTreeClassifier()
    # run(classifier, "Decision tree")

    # Random forest classifier (low accuracy)
    # classifier = RandomForestClassifier()
    # run(classifier, "Random forest")

    # Custom random forest classifier 1
    print "Best classifier for detecting phishing websites."
    classifier = RandomForestClassifier(n_estimators=500, max_depth=15, max_leaf_nodes=10000)
    run(classifier, "Random forest")

    # Linear SVC classifier
    # classifier = svm.SVC(kernel='linear')
    # run(classifier, "SVC with linear kernel")

    # RBF SVC classifier
    # classifier = svm.SVC(kernel='rbf')
    # run(classifier, "SVC with rbf kernel")

    # Custom SVC classifier 1
    # classifier = svm.SVC(decision_function_shape='ovo', kernel='linear')
    # run(classifier, "SVC with ovo shape")

    # Custom SVC classifier 2
    # classifier = svm.SVC(decision_function_shape='ovo', kernel='rbf')
    # run(classifier, "SVC with ovo shape")

    # NuSVC classifier
    # classifier = svm.NuSVC()
    # run(classifier, "NuSVC")

    # OneClassSVM classifier
    print "Worst classifier for detecting phishing websites."
    classifier = svm.OneClassSVM()
    run(classifier, "One Class SVM")

    # print "K nearest neighbours algorithm."
    # nbrs = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree')
    # run(nbrs, "K nearest neighbours")

    # Gradient boosting classifier
    # classifier = GradientBoostingClassifier()
    # run(classifier, "GradientBoostingClassifier")

    # Take user input and check whether its phishing URL or not.
    if len(sys.argv) > 1:
        data_set = generate_data_set(sys.argv[1])

        # Reshape the array
        data_set = np.array(data_set).reshape(1, -1)

        # Load the date
        train_inputs, test_inputs,train_outputs, test_outputs = load_data()

        # Create and train the classifier
        classifier = RandomForestClassifier(n_estimators=500, max_depth=15, max_leaf_nodes=10000)
        classifier.fit(train_inputs, train_outputs)

        print classifier.predict(data_set)
