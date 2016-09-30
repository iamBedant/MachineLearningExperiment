import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


features_train, features_test, labels_train, labels_test = preprocess()

print "Size of features matrix: ", features_train.shape


from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split=40)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = accuracy_score(labels_test, pred)
print "Accuracy: ", acc