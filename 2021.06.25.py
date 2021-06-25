import numpy as np
#np.array([1,2,3,4])



import matplotlib.pyplot as plt     #그래프 그리는 라이브러리(Visualization)
#x = np.array([1,2,3,4])
#plt.plot(x)
#plt.show()

#plt.plot(x, x**2)
#plt.show()

# 그래프에서 한글 처리
# import matplotlib.font_manager as fm
# for font in fm.fontManager.ttflist:
#     print(font.name)   #사용 가능한 폰트 목록 출력
#
# fm.rcParams["font.family"] = "Malgun Gothic"      #Malgun Gothic 선택

# plt.pie  #원 그래프(pie plot)
# data = np.array([1,2,3,4])
# labels = ["A", "B", "C", "D"]
# plt.pie(data, labels=labels)
# plt.show()



#plt.hist #히스토그램  (히스토그램은 막대 그래프와 달리 막대의 폭도 데이터를 표현함)
# np.random.seed(0)
# mu, sigma = 100, 15
# data = mu + sigma * np.random.randn(10000)
# plt.hist(data)
# plt.show()


#플롯 상세 서식에 대해 사용자 지정하기
# x1 = np.arange(5)
# x2 = np.power(x1, 2)
# x3 = np.power(x1, 3)
# plt.plot(x1, "ro-", x2, "b^--", x3, "gs-.")
# plt.title("Title")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.xticks()
# plt.yticks()
# plt.xticks([0, 2, 4])
# plt.yticks([0, 30, 60])
# plt.legend(["x1", "x2", "x3"])
# for f in [x1, x2, x3]:
#     for i, data in enumerate(f):
#         plt.text(i, data + 1.5, data)
# plt.show()
# print(plt.style.availvable)


# plt.style.use("ggplot")
# plt.plot(x1)
# plt.show()
# print(plt.style.available)

# x = np.arange(40)
# plt.subplot(2, 2, 1)
# plt.plot(x, x)
# plt.subplot(2, 2, 2)
# plt.plot(x, x**2, color="red")
# plt.subplot(2, 2, 3)
# plt.plot(x, x**3, color="blue")
# plt.subplot(2, 2, 4)
# plt.plot(x, x**4, color="green")
# plt.show()

#이미지 불러오기
img = plt.imread("cat.jpg")      #이미지를 읽고, numpy객체로 변환
print(img)         #변수를 그대로 출력하면 rgb값을 출력한다.

plt.imshow(img)           #시각적으로 표시
plt.show()