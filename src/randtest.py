import pandas as pd
import random
import math

df = pd.read_csv("Downloads/n_test.csv")
f = open("routput.csv","w+")
f.write("PassengerID,Survived,Prediction\n")
FP = 0
TP = 0
FN = 0
TN = 0
for x in range(df.shape[0]):
	s = df.at[x,"Survived"]
	n = random.randint(0,1)
	if s==1:
		if n==1:
			TP+=1
		else:
			FN+=1
	else:
		if n==1:
			FP+=1
		else:
			TN+=1
	f.write("%d,%d,%d\n" % (df.at[x,"PassengerID"],s,n))
f.close()
TOTAL = FP+FN+TP+TN
print("\___|___\n |%d|%d|\n -------\n |%d|%d|\n -------\n" %(TP,FP,FN,TN))
acc = (TP+TN)/TOTAL
recall = TP/(TP+FN)
spec = TN/(TN+FP)
prec = TP/(TP+FP)
f1 = 2*prec*recall/(prec+recall)
g = math.sqrt(prec*recall)
print("Accuracy: %f" % acc)
print("Recall: %f" % recall)
print("Specificity: %f" % spec)
print("Precision: %f" % prec)
print("F1: %f" % f1)
print("G: %f" % g)
f = open("randresults.csv","a+")
f.write("%f,%f,%f,%f,%f,%f\n" %(acc,recall,spec,prec,f1,g))
