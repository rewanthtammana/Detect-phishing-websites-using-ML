from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

import numpy as np

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

    # Classify the inputs and outputs into training and testing sets
    training_inputs = inputs[:boundary]
    training_outputs = outputs[:boundary]
    testing_inputs = inputs[boundary:]
    testing_outputs = outputs[boundary:]

    # print("Size = " + str(len(training_inputs)) + " .. " + str(training_data.shape) + " :: " + str(len(inputs)) + " -- " + str(len(outputs)) + " [[ ]] " + str(len(testing_outputs)) )

    # Return the four arrays
    return training_inputs, training_outputs, testing_inputs, testing_outputs

def run(classifier, name):
    '''
    Run the classifier to calculate the accuracy score
    '''
    # Load the training data
    train_inputs, train_outputs, test_inputs, test_outputs = load_data()
    # print "Training data loaded."

    # print "Beginning model training."
    # Train the decision tree classifier
    classifier.fit(train_inputs, train_outputs)
    # print "Model training completed."

    # Use the trained classifier to make predictions on the test data
    predictions = classifier.predict(test_inputs)
    # print "Predictions on testing data computed."

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
    classifier = RandomForestClassifier(n_estimators=500, max_depth=15, n_jobs=-1, max_leaf_nodes=10000)
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

    # Gradient boosting classifier
    # classifier = GradientBoostingClassifier()
    # run(classifier, "GradientBoostingClassifier")
