# 홍익대학교 인공지능 팀프로젝트 과제

- **기상관측정보 데이터(수치 데이터) & 위성 사진(이미지 데이터)의 2가지 시계열 데이터를 활용한 날씨 예측**


## 목적
6시간 동안의 연속된 Sequence 데이터(기상관측정보 + 위성사진)를 입력 받았을 때 1시간 뒤의 [기온, 강우랑, 습도] 3가지 기상정보를 예측합니다.


## 사용 데이터
1. 기상청 종관기상관측(ASOS)자료
https://data.kma.go.kr/cmmn/main.do
<img width="651" alt="image" src="https://user-images.githubusercontent.com/89764127/204334624-ac4d3c19-b132-46ce-b0aa-7106e27b1eff.png">

2. 국가기상위성센터 적외 8.7㎛ 구름상 위성사진 데이터 - Open API 사용
<img width="341" alt="image" src="https://user-images.githubusercontent.com/89764127/204334677-f0d1bf83-fc05-477c-932f-c2ea1cef7b9d.png">

- 데이터는 총 24529개
- 위성 문제로 사진이 없는 시간대의 경우 2분, 10분, 30분 전의 데이터 등으로 예외처리


## 사용 Tools
<img width="255" alt="image" src="https://user-images.githubusercontent.com/89764127/204334026-9b68dd2c-d5de-459a-ab76-1f7f3598704b.png"><img width="129" alt="image" src="https://user-images.githubusercontent.com/89764127/204334048-b3cb0d0d-f0bc-4f24-8df1-eb0206449df9.png"><img width="129" alt="image" src="https://user-images.githubusercontent.com/89764127/204334303-3c606f7f-7925-4357-a5fe-3994b2aea43f.png"><img width="275" alt="image" src="https://user-images.githubusercontent.com/89764127/204334082-45d2c344-c894-4594-b97c-a76024777739.png"><img width="250" alt="image" src="https://user-images.githubusercontent.com/89764127/204334100-754e6df7-8ce6-46e2-8d50-190146d6321a.png">



## 데이터 전처리
![image](https://user-images.githubusercontent.com/89764127/204334821-b27d4ad3-ceb9-45f2-a808-343438f38491.png)
- 기상관측정보 데이터
<img width="529" alt="image" src="https://user-images.githubusercontent.com/89764127/204335220-b8d44ae4-4a7e-4d1a-b6ed-ee2ee34fd98b.png">
- 위성 영상 이미지
<img width="607" alt="image" src="https://user-images.githubusercontent.com/89764127/204335336-02578163-f95b-4eab-822c-b3373ff4c6f1.png">



## 최종 구현 모델
CSV 날씨 데이터와 위성 영상 이미지 데이터를 각각의 LSTM 계층에 넣어준 뒤 각각의 output을 평균내는 방식의 모델을 설계했음
<img width="613" alt="image" src="https://user-images.githubusercontent.com/89764127/204335439-4200d32b-9d5f-4302-90b8-7fa56bc25d27.png">



## 최종 모델 예측 결과
<img width="614" alt="image" src="https://user-images.githubusercontent.com/89764127/204336093-6357c087-0ce5-4872-b1e8-8a74743b1b0c.png">

