import os
import csv
import re
import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
from math import log
import warnings
warnings.filterwarnings("ignore")

from konlpy.tag import Hannanum
hn = Hannanum()

df = pd.read_csv("output1.csv")
df2 = pd.read_csv("token_output.csv")

os.getcwd()
os.chdir(r'/Users/sonjimin/Desktop/Project')
docs = df2['token_review']
N=len(docs)

#remove carriage return
def cleancr(dic):
    line = []
    for i in range(len(dic)):
        line.append(re.sub("\s", "", dic[i]))
    return line

#count matches
def matches(dic, d):
    return d.count(dic)


#긍부정어 사전 로딩
f = open("positive.txt", 'r', encoding='UTF8')
positive = f.readlines()
f.close()
positive = cleancr(positive)

f = open("negative.txt", 'r', encoding='UTF8')
negative = f.readlines()
f.close()
negative = cleancr(negative)

#사전비교
N = len(docs)

res = np.zeros(shape=(N, 2), dtype = np.int8)
for i in range(N): #문서별로 수행
    d = docs[i]
    cnt = 0
    for j in range(len(positive)):
        dic = positive[j]        
        cnt += matches(dic, d)
    res[i, 0] = cnt

for i in range(N): #문서별로 수행
    d = docs[i]
    cnt = 0
    for j in range(len(negative)):
        dic = negative[j]        
        cnt += matches(dic, d)
    res[i, 1] = cnt
    
    
positive=[]
for i in range(N):
    res
    pos_rate = res[:, 0] / (res[:, 0] + res[:, 1])  #긍정도 계산
    positive.append(pos_rate) #하나의 리스트를 만들어서 한번에 df에 추가해야함.
    df2['positive']=pos_rate #형태소단위로 나누어진 리뷰저장

df3=df2.drop(df2.columns[2], axis='columns')
df3.to_csv('positive_rate.csv', encoding='utf-8-sig', mode='w')
        

print(df3)
