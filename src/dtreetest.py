import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import export_text
df = pd.read_csv("Downloads/n_train.csv")
df2 = pd.read_csv("Downloads/n_test.csv")
X_sub = df.drop("Survived", axis=1)
X_train = X_sub.drop("PassengerID",axis=1)
Y_train = df["Survived"]
X_test = df2.drop("Survived", axis=1)
X_test = X_test.drop("PassengerID",axis=1)
Y_test = df2["Survived"]
dtc = DecisionTreeClassifier()
dtc.fit(X_train,Y_train)
Y_pred = dtc.predict(X_test)
print(confusion_matrix(Y_test,Y_pred))
print(classification_report(Y_test,Y_pred))
r = export_text(dtc,feature_names=list(X_train.columns))
print(r)
