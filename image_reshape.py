### 이미지 전처리 테스트 코드
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread("/Users/kim-youngbin/Desktop/Hongik/AI/team_proj/images/2019123123.png", cv2.IMREAD_COLOR)

# 원본 shape
print(img.shape)    # (922, 900, 3)

# matplotlib와 opencv에서의 rgb 채널 순서가 다름
# opencv -> blue / red / green
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB 순서로 변환

# 채널 분리 -> r: red 채널, g: green 채널, b: blue 채널
# 채널 이미지 (922, 900, 1) -> blue가 사용하기 적합
r, g, b = cv2.split(fix_img)

# 이미지 자르기
b = b[160:730, 300:670]
# plt.imshow(b)
# plt.show()
print(b.shape)

# 사이즈 줄이기
resized = cv2.resize(b, dsize=(224, 224), interpolation=cv2.INTER_AREA)
plt.imshow(resized)
plt.show()
print(resized.shape)


# # 테스트 하는 방법 -> 이미지 보여줌
# # cv2.imshow("src", b)
# # cv2.waitKey()
# # cv2.destroyAllWindows()







# # GrayScale로 불러오기
# img_gray = cv2.imread("2019123123.png", cv2.IMREAD_GRAYSCALE)   # grayscale
# print(img_gray.shape)   # (922, 900)

# plt.imshow(img_gray, cmap='gray')
# plt.show()