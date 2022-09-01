# -*- coding: utf-8 -*-
"""group14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zrrjjnXcp_IDmrYxYKnz3a2kdvZ5WdGw

# Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""# Arranging Train and Test Datasets

## Importing Datasets
"""

Train=pd.read_csv("train.csv")
Test=pd.read_csv("test.csv")

print(Train.head())
print(Test.head())

"""## Rearranging and Discovering Datasets

### Getting Column Values
"""

columns=str(Train.columns[0]).split("|")
print(columns)

"""### Getting Train Features by using Split"""

new_train=[]

for i in Train.iloc:
  new_train.append(i[0].split("|"))

train_data=pd.DataFrame(new_train,columns=columns)
train_data.head()

train_data.describe()

"""### Getting Test Features by Split"""

new_test=[]

for i in Test.iloc:
  new_test.append(i[0].split("|"))

test_data=pd.DataFrame(new_test,columns=columns[:-1])
test_data.head()

test_data.describe()

"""## Controlling Normalized Data"""

for i in columns:
    print(i,np.max(train_data[i]))

train_data.head()

"""# Applying Different Types of Classification Techniques

### Splitting Data into Train and Test Parts
"""

X=train_data.iloc[:,:-1]
y=train_data.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

"""### KNN"""

from sklearn.neighbors import KNeighborsClassifier

acc_scores_knn=[]
distance=[] 
K=range(1,16)

for k in K:
  knn=KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train,y_train)
  pred=knn.predict(X_test)
  acc_scores_knn.append(accuracy_score(y_test,pred))
  distance.append(np.mean(pred != y_test))

plt.plot(K,acc_scores_knn,"-x",color="red")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy Scores")
plt.title("KNN Accuracy Scores")
plt.show()

plt.plot(K,distance,"-x",color="red")
plt.xlabel("Number of Neighbors")
plt.ylabel("Distance")
plt.title("Cluster Values and Distances")
plt.show()

"""### Naive Bayes"""

from sklearn.naive_bayes import GaussianNB,MultinomialNB,ComplementNB,BernoulliNB,CategoricalNB

"""###### Gaussian NB"""

gnb=GaussianNB().fit(X_train,y_train)
pred=gnb.predict(X_test)
acc_scores_gnb=(accuracy_score(y_test,pred))
print("Gaussian NB accuracy score:",acc_scores_gnb)

"""###### Multinominal NB"""

mnb=MultinomialNB().fit(X_train,y_train)
pred=mnb.predict(X_test)
acc_scores_mnb=(accuracy_score(y_test,pred))
print("Multinominal NB accuracy score:",acc_scores_mnb)

"""###### Complement NB"""

compnb=ComplementNB().fit(X_train,y_train)
pred=compnb.predict(X_test)
acc_scores_comnb=(accuracy_score(y_test,pred))
print("Complement NB accuracy score:",acc_scores_comnb)

"""###### Bernoulli NB"""

bnb=BernoulliNB().fit(X_train,y_train)
pred=bnb.predict(X_test)
acc_scores_bnb=(accuracy_score(y_test,pred))
print("Bernoulli NB accuracy score:",acc_scores_bnb)

acc_scores_nbs=[acc_scores_gnb,acc_scores_mnb,acc_scores_comnb,acc_scores_bnb]
models=["Gaussian NB","Multinominal NB","Complement NB","Bernoulli NB"]

fig=plt.figure(figsize=(7,5))
plt.plot(models,acc_scores_nbs,"-x")
plt.xlabel("Navie Bayes Models")
plt.ylabel("Accuracy Scores")
plt.title("Accuray Scores for Different Naive Bayes Algorithms")
plt.show()

"""### Logistic Regression"""

from sklearn.linear_model import LogisticRegression

acc_scores_lr=[]

solvers=["newton-cg","lbfgs","sag","saga","liblinear"]

for solver in solvers:
  lr=LogisticRegression(solver=solver,multi_class="ovr",max_iter=200)
  lr.fit(X_train,y_train)
  pred=lr.predict(X_test)
  acc_scores_lr.append(accuracy_score(y_test,pred))

plt.plot(solvers,acc_scores_lr,"-x",color="yellow")
plt.xlabel("Solver Types")
plt.ylabel("Accuracy Scores")
plt.title("Accuracy Scores for Different Solver Types")
plt.show()

"""### MLP"""

from sklearn.neural_network import MLPClassifier

mlp=MLPClassifier()
mlp.fit(X_train,y_train)
mlp_pred=mlp.predict(X_test)

print("Accuracy score:",accuracy_score(y_test,mlp_pred))

"""### Random Forest"""

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier(max_features=5,n_estimators=500)
rfc.fit(X_train,y_train)
rfc_pred=rfc.predict(X_test)

print("Accuracy score:",accuracy_score(y_test,rfc_pred))

"""### Support Vector Machine"""

from sklearn.svm import SVC

svm_model=SVC(gamma="auto").fit(X_train,y_train)
pred=svm_model.predict(X_test)

print("Accuracy score:",accuracy_score(y_test,pred))

"""# Choosing The Best Model and Getting Results

"""

rfc_test_pred=rfc.predict(test_data)

rf=[int(each) for each in rfc_test_data]

mlp_test_pred=mlp.predict(test_data)

ml=[int(each) for each in mlp_test_data]

bnb_test_pred=bnb.predict(test_data)

bn=[int(each) for each in bnb_test_data]

lr_test_pred=lr.predict(test_data)

l=[int(each) for each in lr_test_data]

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,y_train)

knn_test_pred=knn.predict(test_data)

kn=[int(each) for each in knn_test_data]

svm_test_pred=svm_model.predict(test_data)

sv=[int(each) for each in svm_test_data]

print(len(rfc_test_pred),"rfc preds:",sum(rf),"mlp preds:",sum(ml),"mnb preds:",sum(bn),"lr preds:",sum(l),"knn preds:",sum(kn),"svm preds:",sum(sv))

"""# Choosing Machine Learning Algorithm"""

preds=rfc.predict(test_data)

preds_df=pd.DataFrame(preds,columns=["fraud"])

preds_df.to_csv("group14_predictions.csv")