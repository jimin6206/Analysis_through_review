#패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os

name=['에어팟 1세대']
category=['만족도','가격','음질','디자인','사용성','품질','성능','기능']

#에어팟 1세대 검색 
ns_address_airpod="https://search.shopping.naver.com/detail/detail.nhn?nvMid=10776906666&query=%25EC%2597%2590%25EC%2596%25B4%25ED%258C%259F%25201%25EC%2584%25B8%25EB%258C%2580&NaPm=ct%3Dkb3ef8sg%7Cci%3Df7d5699aba286396ee3757965561aa228125c722%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Da9cfdf21495248f435f4ae3cbea263c694784ae1"
#xpath
shoppingmall_review='/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/ul/li[4]/a/strong'
category1="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[2]/a" #만족도
category2="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[3]/a" #가격 
category3="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[4]/a" #음질
category4="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[5]/a" #디자인
category5="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[6]/a" #사용성
category6="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[7]/a" #품질
category7="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[8]/a" #성능
category8="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[9]/a" #기능

header = {'User-Agent': ''}
d = webdriver.Chrome('/Users/sonjimin/Desktop/Project/chromedriver') # webdriver = chrome
d.implicitly_wait(3)
d.get(ns_address_airpod)
req = requests.get(ns_address_airpod)
html = req.text 
soup = BeautifulSoup(html, "html.parser")

#함수 선언
def add_dataframe(name,category,reviews,stars,cnt):  #데이터 프레임에 저장
    #데이터 프레임생성
    df1=pd.DataFrame(columns=['type','category','review','star'])
    n=1
    if (cnt>0):
        for i in range(0,cnt-1):
            df1.loc[n]=[name,category,reviews[i],stars[i]] #해당 행에 저장
            i+=1
            n+=1
    else:
        df1.loc[n]=[name,category,'null','null']
        n+=1    
    return df1

def save():
    if not os.path.exists('output1.csv'):
        df1.to_csv('output1.csv', encoding='utf-8-sig', mode='w')
    else:
        df1.to_csv('output1.csv',encoding='utf-8-sig', mode='a',header=False)

def review_data(category,category_name) :
    d.find_element_by_class_name('filter_evaluation_tap__-45pp').click()
    d.find_element_by_xpath(category).click() #스크롤 건드리면 안됨
    name_=name[0]  #에어팟 1세대
    category_= category_name
    reviews=[]
    stars=[]
    cnt=1   #리뷰index
    page=1
    while (cnt<1000):  #1000개씩 가져오기 
        j=1
        print ("페이지", page ,"\n")
        sleep(2)
        while True: #한페이지에 20개의 리뷰, 마지막 리뷰에서 error발생
            try:
                star=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/ul/li['+str(j)+']/div[1]/span').text 
                stars.append(star[2])
                review=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/ul/li['+str(j)+']/div[2]/div[1]/p').text
                reviews.append(review)
                if j%2==0: #화면에 2개씩 보이도록 스크롤
                    ELEMENT = d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/ul/li['+str(j)+']/div[2]')
                    d.execute_script("arguments[0].scrollIntoView(true);", ELEMENT)       
                j+=1
                print(cnt, review ,star, "\n")
                cnt+=1 
            except: break
            
        sleep(2)
    
        if page<11:#page10까지 적용
            try: #리뷰의 마지막 페이지에서 error발생
                next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[3]/a['+str(page+1)+']').click() 
                page +=1
            except: break #리뷰의 마지막 페이지에서 process 종료
            
        else:
            try: #page11부터
                if page%10==0:
                    next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[3]/a[12]').click()
                else :
                    next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[3]/a['+str(page%10+2)+']').click()
                page+=1
            except: break 
        
            
    df1=add_dataframe(name_,category_,reviews,stars,cnt)
    return df1

#쇼핑몰 리뷰 보기
d.find_element_by_class_name('totalArea_total_area__NRExb').click()
d.find_element_by_xpath(shoppingmall_review).click()
sleep(2)


#리뷰 가져오기
df1 = review_data(category1, "만족도")
save()
df1 = review_data(category2, "가격")
save()
df1 = review_data(category3, "음질")
save()
df1 = review_data(category4, "디자인")
save()
df1 = review_data(category5, "사용성")
save()
df1 = review_data(category6, "품질")
save()
df1 = review_data(category7, "성능")
save()
df1 = review_data(category8, "기능")
save()
