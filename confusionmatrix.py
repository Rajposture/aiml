from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import recall_score, f1_score

actual = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]
predicted = [1, 1, 0, 0, 0, 1, 1, 0, 1, 0]

cm = confusion_matrix(actual, predicted)

print("Confusion Matrix:")
print(cm)

print("Accuracy:", accuracy_score(actual, predicted))
print("Precision:", precision_score(actual, predicted))
print("Recall:", recall_score(actual, predicted))
print("F1 Score:", f1_score(actual, predicted))