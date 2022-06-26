import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
import re
import nltk
from konlpy.tag import Okt; t= Okt()

def clean_str(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text   

#크롤링 한 output1.csv 불러오기 
df = pd.read_csv("output1.csv")

#불용어 제거
text=''
review=[]
for each_line in df['review']:
    review.append(each_line)

review_=[]
for i in review:
    a=clean_str(i)
    review_.append(a)


#형태소 분석 
a = len(review_)
token_review_list=[]

for i in range(0,a): # 리뷰하나당 처리하기위해 for문 
    token_review=t.morphs(review_[i])  #t=형태소분석기. morphs=형태소 추출.review_=전처리한 리뷰.
    token_review_list.append(token_review) #하나의 리스트를 만들어서 df에 추가해야함.
df['token_review']=token_review_list #형태소단위로 나누어진 리뷰저장

df.to_csv('token_output.csv', encoding='utf-8-sig', mode='w')

df_sorted_by_star = df.sort_values(by='star', ascending=False)

adf=df_sorted_by_star.groupby('star').count()


##별점별 리뷰 개수
##print(adf)

five_review=[]
five_token_review=[]
for i in range(0,2877):
    if(df['star'][i]==5):
        five_review.append(df['review'][i])  #5점리뷰모음. len=725
        five_token_review.append(df['token_review'][i])

#단어 빈도수 계산
frequency = {}

for token_review in five_token_review:
    for word in token_review:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        
sort=sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print(sort)

