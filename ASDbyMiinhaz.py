# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:02:37 2022

@author: Miinhaz
"""
#Importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import numpy as np


# Importing the DATASET and dropping unneccesary columns and some plots
asd = pd.read_csv('Toddler_Autism.csv')
print(asd['Ethnicity'].value_counts())
sns.countplot(x='Class/ASD Traits ' , data=asd)
asd.drop(['Case_No','Qchat-10-Score'], axis = 1, inplace = True)
asd.columns

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
columns = ['Ethnicity', 'Who completed the test' , 'Family_mem_with_ASD', 'Class/ASD Traits ', 'Sex', 'Jaundice']
for col in columns:
    asd[col] = le.fit_transform(asd[col])
#print(asd.dtypes)

# X and Y matrix formation
X = asd.drop(['Class/ASD Traits '], axis = 1)
Y = asd['Class/ASD Traits ']

#for differentiate the ethnicities
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [12])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


# Train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.30, random_state = 40)

#for better accuracy
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.transform(x_test)


#******************************LOGISTIC REGRESSION ***********************************#
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='lbfgs', max_iter=1000)
#the default solver in LogisticRegression is 'lbfgs'
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print('for logistic regression= \n',cm)
from sklearn.metrics import accuracy_score
print('for Logistic Regression the accuracy is= ',accuracy_score(y_test, y_pred))



#*****************************DECISION TREE CLASSIFIER ***********************************#
from sklearn.tree import DecisionTreeClassifier
classifier1 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier1.fit(x_train, y_train)
# Predicting the Test set results
y_pred1 = classifier1.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred1)
print('for random tree classifier= \n',cm)
print('for Random Tree Classifier the accuracy is= ',accuracy_score(y_test, y_pred1))



#*************************************SVM ***********************************#
from sklearn.svm import SVC
classifier2 = SVC()
classifier2.fit(x_train, y_train)
y_pred2 = classifier2.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred2)
print('for SVM= \n' ,cm)
print('for SVM the accuracy is= ',accuracy_score(y_test, y_pred2))


#**************************RANDOM FOREST CLASSIFIER ***********************************#
from sklearn.ensemble import RandomForestClassifier
classifier3 = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier3.fit(x_train, y_train)

# Predicting the Test set results
y_pred3 = classifier3.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred3)
print('for random forest classification= \n' ,cm)
print('for Random forest Classification the accuracy is= ',accuracy_score(y_test, y_pred3))


#******************************NAIVE BAYES ***********************************#
from sklearn.naive_bayes import GaussianNB
classifier4 = GaussianNB()
classifier4.fit(x_train, y_train)
y_pred4 = classifier4.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred4)
print('for naive bayes= \n',cm)
print('for Naive bayes the accuracy is= ',accuracy_score(y_test, y_pred4))



#****************************** KNEIGHBOURS CLASSIFIER***********************************#
from sklearn.neighbors import KNeighborsClassifier
classifier5 = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier5.fit(x_train, y_train)

# Predicting the Test set results
y_pred5 = classifier5.predict(x_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred5)
print('for KNeighbour Classifier= \n',cm)
print('for KNeighbour Classifier the accuracy is= ',accuracy_score(y_test, y_pred5))



# Saving model to disk
pickle_out=open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

pickle_out=open("classifier2.pkl","wb")
pickle.dump(classifier2, pickle_out)
pickle_out.close()

pickle_out=open("classifier3.pkl","wb")
pickle.dump(classifier3, pickle_out)
pickle_out.close()

pickle_out=open("classifier4.pkl","wb")
pickle.dump(classifier4, pickle_out)
pickle_out.close()

pickle_out=open("classifier5.pkl","wb")
pickle.dump(classifier5, pickle_out)
pickle_out.close()

#pickle.dump(classifier, open('model.pkl','wb'))

#for other purposes
# Loading model to compare the results
#model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2, 9, 6]]))