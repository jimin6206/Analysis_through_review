import os
import csv
import re
import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
from math import log
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore")

df3 = pd.read_csv("positive_rate.csv")

N = len(df3)

pos =[]
result = []

pos = df3['positive']

df3 = df3.fillna(0.5)

for i in range(N) :
    
    if pos[i] >= 0.5 :
        result.append(1)
    else :
        result.append(0)

df3['result'] = result
        
df4=df3.drop(df3.columns[2], axis='columns')
df4.to_csv('result.csv', encoding='utf-8-sig', mode='w')

X, y = df4[['positive']], df4['result']

X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)


log_clf = LogisticRegression(random_state=42)
log_clf.fit(X_train, y_train)
y_pred = log_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("accuracy : ", accuracy)


sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0

for i in range(0,2877):
    if(df4['category'][i]=="만족도"):
        sum1 += df4['positive'][i]
        count1 +=1
    if(df4['category'][i]=="가격"):
        sum2 += df4['positive'][i]
        count2 +=1
    if(df4['category'][i]=="음질"):
        sum3 += df4['positive'][i]
        count3 +=1
    if(df4['category'][i]=="디자인"):
        sum4 += df4['positive'][i]
        count4 +=1
    if(df4['category'][i]=="사용성"):
        sum5 += df4['positive'][i]
        count5 +=1
    if(df4['category'][i]=="품질"):
        sum6 += df4['positive'][i]
        count6 +=1
    if(df4['category'][i]=="성능"):
        sum7 += df4['positive'][i]
        count7 +=1
    if(df4['category'][i]=="기능"):
        sum8 += df4['positive'][i]
        count8 +=1
        

ave1 = sum1/count1
ave2 = sum2/count2
ave3 = sum3/count3
ave4 = sum4/count4
ave5 = sum5/count5
ave6 = sum6/count6
ave7 = sum7/count7
ave8 = sum8/count8

print(ave1)
print(ave2)
print(ave3)
print(ave4)
print(ave5)
print(ave6)
print(ave7)
print(ave8)






