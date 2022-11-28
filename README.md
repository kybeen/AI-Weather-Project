# 홍익대학교 인공지능 팀프로젝트 과제
기상관측정보 데이터(수치 데이터) & 위성 사진(이미지 데이터)의 2가지 시계열 데이터를 활용한 날씨 예측

---
## 목적
6시간 동안의 연속된 Sequence 데이터(기상관측정보 + 위성사진)를 입력 받았을 때 1시간 뒤의 [기온, 강우랑, 습도] 예측

---
## 사용 데이터
1. 기상청 종관기상관측(ASOS)자료
https://data.kma.go.kr/cmmn/main.do
<img width="344" alt="image" src="https://user-images.githubusercontent.com/89764127/204332658-61f975dd-5266-4e8f-a120-10a8a2364613.png">

2. 국가기상위성센터 적외 8.7㎛ 구름상 위성사진 데이터 - Open API 사용
<img width="360" alt="image" src="https://user-images.githubusercontent.com/89764127/204332485-9fa8f0a1-4a24-455a-9bef-c82c40eaffa7.png">

- 위성 문제로 사진이 없는 시간대의 경우 2분, 10분, 30분 전의 데이터 등으로 예외처리

---
## 사용 Tools
<img width="255" alt="image" src="https://user-images.githubusercontent.com/89764127/204334026-9b68dd2c-d5de-459a-ab76-1f7f3598704b.png">
<img width="129" alt="image" src="https://user-images.githubusercontent.com/89764127/204334048-b3cb0d0d-f0bc-4f24-8df1-eb0206449df9.png">
![image](https://user-images.githubusercontent.com/89764127/204334064-4728a5c0-63f6-46bb-96f9-70f29f87de59.png)
<img width="275" alt="image" src="https://user-images.githubusercontent.com/89764127/204334082-45d2c344-c894-4594-b97c-a76024777739.png">
<img width="250" alt="image" src="https://user-images.githubusercontent.com/89764127/204334100-754e6df7-8ce6-46e2-8d50-190146d6321a.png">
