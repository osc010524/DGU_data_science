# 조건문
i = True
if (i):
    print("참")
else:
    print("거짓")
# 반복문
data = ["Apple", "Banana", "Cherry", "Date", "Fig"]
for i in data:
    print(i.upper())
    if i == "Cherry":
        continue  # 다음 반복으로 넘어감
    elif i == "Date":
        break  # 반복문 종료

while True:
    if i == "Date":
        break
# 일반적인 함수
a = 1  # 전역변수


def func(a, b):
    c = a + b  # 지역변수
    return c


# 입력값이 없는 함수
def func():
    print("Hello")


# # 파일 입출력
# f = open("test.txt", "rw")
# f.write("Hello")
# f.close()

# 반복문 내포
# 간결한 표현으로 새로운 리스트 만들 수 있음
data_upper = [i.upper() for i in data]

# enumerate : 리스트 요소 변경 가능
for i, j in enumerate(data):
    data[i] = j.upper()
print(data)

# 리스트 슬라이싱
data = [1, 2, 3, 4, 5]
print(data[1:3])  # 2, 3
print(data[:3])  # 1, 2, 3
print(data[3:])  # 4, 5
print(data[-1])  # 5
print(data[:-1])  # 1, 2, 3, 4
print(data[1:4:2])  # 2, 4
print(data[1::2])  # 2, 4
# 리스트 복사
data2 = data[:]  # 리스트 복사 : shallow copy
data3 = [i for i in data]  # 리스트 복사 : deep copy
data4 = data.copy()  # 리스트 복사 : deep copy
data5 = [data] * 3  # 리스트 복사 : shallow copy

print(data5)
for i in data5:
    print(id(i))
data5[1][1] = 9
print(data5)

#
#
# import csv
# # CSV 파일 읽기
# with open('data/data1.csv', 'r', encoding='cp949') as f:
#     dat = [k for k in csv.reader(f)] # 리스트 컴프리헨션을 사용한다
# # CSV 파일 쓰기
# with open('data/out.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(dat)
#
#
# import numpy as np
#
# # CSV 파일 읽기
# dat = np.loadtxt(open('data/data1.csv','rb'), delimiter=',', skiprows=1, dtype=float)
# # CSV 파일 읽기2
# dat = np.genfromtxt(open('data/data1.csv','rb'), skip_header=1, delimiter=',', dtype=float)
# # 구분자는 ,(콤마), 첫 줄은 건너뜀(skiprows=1), 부동 소수 타입으로(dtype=float(기본값))
#
# #배열/행렬
# data_ndarray = np.array([1,2], [3,4], [5,6], [7,8])
# data_matrix = np.matrix([[1,2], [3,4], [5,6], [7,8]])
#
# data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# # 2차원 배열 슬라이싱 => 넘파이에만 있는 기능
# print(data[:, 1])  # 2, 4, 6, 8
#
# data2 = np.array([(1, 2), (3, 4), (5, 6), (7, 8)])
# print(data2) # 튜플이 리스트로 바뀜
#
# data_zero = np.zeros((2, 3))  # 2행 3열의 0으로 채워진 배열
# data_ones = np.ones((2, 3))  # 2행 3열의 1로 채워진 배열
# data_arange = np.arange(10,20,2)  # 10부터 20까지 2씩 증가하는 배열
#
# # 그래프 그리기
# import matplotlib.pyplot as plt
# datal = [1, 2, 3, 4, 5]
# datay = [2, 3, 4, 5, 6]
# plt.scatter(datal, datay)
# # 점 찍기
# plt.scatter(3, 3, color='red')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
#
# import pandas as pd
# # CSV 파일 읽기
# dat = pd.read_csv('data/data1.csv')
# # CSV 파일 쓰기
# dat.to_csv('data/out.csv', index=False)
#
# # 데이터프레임
# data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
# df = pd.DataFrame(data)
# # series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
#
#
#
#
#
