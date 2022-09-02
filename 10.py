# The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature value, labeled f. Note that there are two data points with the same feature value of 9. These are shown as two x's one above the other.
# Divide this data equally into two parts. Use first part as training and second part as testing. Using KNN classifier, for K = 3, what would be the predicted outputs for the test sample? Show how you arrived at your answer.
x = [1, 2, 3, 6, 6, 7, 10, 11]
data = [1, 1, 0, 0, 0, 1, 1, 1]
first = [0, 1, 2, 3]
second = [4, 5, 6, 7]

from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors=3)
x_train = [[x[t]] for t in first]
y_train = [[data[t]] for t in first]
regressor.fit(x_train, y_train)
x_test = [[x[t]] for t in second]
y_test = [[data[t]] for t in second]
y_pred = regressor.predict(x_test)
y_ = []
for i in range(len(y_pred)):
	if y_pred[0] > 0.1:
		y_.append(1)
	else:
		y_.append(0)
print("Predict value: ")
print(y_)

# Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity values.
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
conf = confusion_matrix(y_, y_test)
print("Confusion Matrix")
print(conf)

accuracy = accuracy_score(y_, y_test)
print("Accuracy: ", accuracy)

sensetivity = conf[0][0] / (conf[0][0] + conf[0][1])
print("Sensitivity: ", sensetivity)

specificity = conf[0][0] / (conf[0][0] + conf[1][0])
print("Specificity: ", specificity)
