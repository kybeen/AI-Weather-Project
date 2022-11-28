### 위성사진 이미지 전처리 코드


# import os
# import cv2
# import matplotlib.pyplot as plt

# path = '/Users/kim-youngbin/Desktop/Hongik/AI/team_proj/images/'    # 이미지 파일 경로
# os.chdir(path) # 해당 폴더로 이동
# files = os.listdir(path)    # 해당 폴더에 있는 파일 이름 리스트 형태로 받음
# files.sort()    # 파일 이름 순서대로 정렬
# # print(files)
# print(len(files))

# # 이미지 가공
# weather_images = [] # 가공된 이미지 담을 배열
# for i in range(len(files)):
#     img = cv2.imread(files[i], cv2.IMREAD_COLOR)    # 파일 이름 리스트를 사용하여 이미지 컬러로 받아옴 (900, 900, 3)
#     # # 이미지 누락 확인
#     # print(img.shape)
#     # print(i)
#     fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # opencv로 불러오는 이미지는 Blue / Red / Green 순서임  ==>  RGB로 바꿔줌

#     r, g, b = cv2.split(fixed_img)    # Blue 채널 추출 (900, 900)
#     b = b[140:730, 300:670] # Blue 채널 이미지 자르기
#     resized_b = cv2.resize(b, dsize=(224, 224), interpolation=cv2.INTER_AREA)   # 해상도 (224 x 224)로 축소

#     weather_images.append(resized_b)

# # 확인용 코드
# print(len(weather_images))
# print(weather_images[0].shape)  # (224, 224)
# plt.imshow(weather_images[0])
# plt.show()




# # 하나만 확인해보는 코드
# print(files[0]) # 2019072500.png
# img = cv2.imread(files[0], cv2.IMREAD_COLOR)    # 파일 이름 리스트를 사용하여 이미지 컬러로 받아옴 (922, 900, 3)
# plt.imshow(img)
# plt.show()
# print(img.shape) # (900, 900, 3)
# fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # opencv로 불러오는 이미지는 Blue / Red / Green 순서임  ==>  RGB로 바꿔줌
# plt.imshow(fixed_img)
# plt.show()

# r, g, b = cv2.split(fixed_img)    # Blue 채널 추출 (900, 900)
# print(b.shape)  # (900, 900)
# b = b[140:730, 300:670] # Blue 채널 이미지 자르기
# plt.imshow(b)
# plt.show()
# resized_b = cv2.resize(b, dsize=(224, 224), interpolation=cv2.INTER_AREA)   # 해상도 (224 x 224)로 축소
# print(resized_b.shape)  # (224, 224)
# # 가공된 이미지 확인
# plt.imshow(resized_b)
# plt.show()




# TEST
# import os
# import cv2
# import matplotlib.pyplot as plt

# path = '/Users/kim-youngbin/Desktop/Hongik/AI/team_proj/images'
# file = '2019123123.png'

# os.chdir(path)

# img = cv2.imread(file, cv2.IMREAD_COLOR)  # 파일 이름 리스트를 사용하여 이미지 컬러로 받아옴 (900, 900, 3)
# plt.imshow(img)
# plt.show()
# # # 이미지 누락 확인
# # print(img.shape)
# # print(i)
# fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # opencv로 불러오는 이미지는 Blue / Red / Green 순서임  ==>  RGB로 바꿔줌
# plt.imshow(fixed_img)
# plt.show()

# r, g, b = cv2.split(fixed_img)  # RGB 이미지에서 Blue 채널 추출 (900, 900)
# plt.imshow(r)
# plt.show()
# plt.imshow(g)
# plt.show()
# plt.imshow(b)
# plt.show()

# b = b[140:730, 300:670] # Blue 채널 이미지 한반도에 맞춰서 자르기
# plt.imshow(b)
# plt.show()

# resized_b = cv2.resize(b, dsize=(100, 100), interpolation=cv2.INTER_AREA)  # 해상도 (100 x 100)로 축소
# plt.imshow(resized_b)
# plt.show()



import cv2
import matplotlib.pyplot as plt

# 기존 이미지 (922, 900, 3)
src = cv2.imread("/Users/kim-youngbin/Desktop/Hongik/AI/team_proj/images/2019123123.png", cv2.IMREAD_COLOR)
print(src)
# 채널 분리 -> b: blue 채널, g: green 채널, r: red 채널, b: blue 채널
# 채널 이미지 (922, 900, 1) -> blue가 사용하기 적합
src = src[22:922, :]
# plt.imshow(src)
# plt.show()
cv2.imshow("Origin", src)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.destroyAllWindows()
# plt.imshow(src)
# plt.show()
fixed_img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# plt.imshow(fixed_img)
# plt.show()
cv2.imshow("fixed_img", fixed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(src)
# plt.imshow(b)
# plt.show()
cv2.imshow("Blue", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

b = b[140:730, 300:670] # Blue 채널 이미지 한반도에 맞춰서 자르기
# plt.imshow(b)
# plt.show()
cv2.imshow("Blue", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized_b = cv2.resize(b, dsize=(100, 100), interpolation=cv2.INTER_AREA)   # 해상도 (224 x 224)로 축소
# plt.imshow(resized_b)
# plt.show()
cv2.imshow("Resized", resized_b)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(resized_b))
print(type(resized_b[0]))
print(type(resized_b[0][0]))

# cv2.imshow("g", g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("r", r)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.destroyAllWindows()
# plt.imshow(b)
# plt.show()
# plt.imshow(g)
# plt.show()
# plt.imshow(r)
# plt.show()