![header](https://capsule-render.vercel.app/api?type=wave&color=fddedf&height=230&section=header&text=Analysis_through_review%20render&fontSize=50&fontColor=9e9e9e)

# 쇼핑몰 리뷰를 통한 상품 분석

## 연구배경

Review란? 제품에 만족한 이유를 드러내는 비정형 데이터이며 소비자의 솔직하고, 의도되지 않은 데이터이다.

사장님이나 소비자들은 리뷰를 통해 많은 정보를 얻는다. 하지만 많은 리뷰를 일일이 읽어봐야 하는 단점이 있다. 감정사전을 통해 리뷰를 분석해서 카테고리별로 긍정 리뷰인지 부정 리뷰인지를 한눈에 볼 수 있다면 쉽게 정보를 얻을 수 있다.

## 연구과정
+ 데이터 수집
  + 네이버 쇼핑 AirPods 리뷰

+ 데이터 전처리
  + 불용어 제거 -> 형태소 분석 -> 빈도수 분석으로 긍정&부정 사전 생성

+ 데이터 분석
  + 생성된 긍정&부정어 사전으로 감정 분석 진행 후 긍정도 비교

## 네이버 쇼핑몰 리뷰
![image](https://user-images.githubusercontent.com/75300624/175827208-3e61cd95-dcee-4e20-9611-8dc2661a72dc.png)

네이버 쇼핑은 'AirPods'을 판매하는 모든 사이트의 리뷰를 볼 수 있다.

리뷰의 주제 별로 카테고리화 되어있다.


## 데이터 수집 -> 크롤링
![image](https://user-images.githubusercontent.com/75300624/175827036-4a9ce8db-2b10-4bbc-a146-b5152d73f9eb.png)

카테고리별로 리뷰데이터 저장

![image](https://user-images.githubusercontent.com/75300624/175827057-3deaa328-6cd1-4af4-961e-eb48e551d200.png)

모든 리뷰 데이터를 csv파일로 저장

## 불용어 제거
![image](https://user-images.githubusercontent.com/75300624/175827339-60302bba-d8d3-402e-92a8-c1685b11b1d8.png)

불용어 제거 코드

![image](https://user-images.githubusercontent.com/75300624/175827344-c1b7c469-b9ae-4577-9dcc-861b5e19f106.png)

불용어 제거 전 / 후 비교

## 형태소 분석
![image](https://user-images.githubusercontent.com/75300624/175827373-3613dc7a-f57e-4057-8b64-d104ce224cbe.png)

형태소 분석 코드

![image](https://user-images.githubusercontent.com/75300624/175827381-c71b0c8c-7596-459d-adda-fbcb5878fbe8.png)

텍스트 리뷰가 토큰화 되어 저장됨

## 별점 별 리뷰
![image](https://user-images.githubusercontent.com/75300624/175827405-b7e4f4ba-9395-4c72-9d18-70f05d279b87.png)

별점 별 리뷰 개수 확인하기

![image](https://user-images.githubusercontent.com/75300624/175827429-4cfafca9-17ca-493a-8a1c-147f930ae15e.png)

별점 별로 단어 빈도수 출력

## 긍정 / 부정 사전
![image](https://user-images.githubusercontent.com/75300624/175827465-54c3a45e-7c3b-493b-a19c-9ff2f22938b5.png)

## 긍정도 계산
![image](https://user-images.githubusercontent.com/75300624/175827486-39d26720-3bb4-4222-a66e-2ccf8d8c2c46.png)

## 결과
![image](https://user-images.githubusercontent.com/75300624/175827497-8a5ea960-a595-491a-bcd7-54f61da62ed5.png)


![Footer](https://capsule-render.vercel.app/api?type=wave&color=fddedf&height=200&section=footer)
