import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 35 개 도미 (bream) 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# 14개 빙어(smelt) 데이터
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 도미와 빙어 데이터 합치기
fish_length = bream_length + smelt_length
fish_weight = bream_weight + smelt_weight

# #도미와 빙어 데이터 합쳐서 산점도 시각화 코딩
# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight, color = 'red')
#
# plt.show()

fish_data = np.column_stack((fish_length, fish_weight))
fish_target = [1] * 35 + [0] * 14

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# 데이터 랜덤하게 섞기
np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

# 랜덤하게 섞인 데이터 시각화
# plt.scatter(train_input[:,0], train_input[:,1], color = 'blue')
# plt.scatter(test_input[:,0], test_input[:,1], color = 'red')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

kn = KNeighborsClassifier()
# 훈련
kn.fit(train_input, train_target)
# 평가
kn.score(test_input, test_target)
# 결과
ans = kn.predict(test_input)
# print(ans)

for i in range(len(test_input)):
    print(
        f'length: {test_input[i][0]}, weight: {test_input[i][1]}, real: {test_target[i]}, predict: {ans[i]}, result : {True if test_target[i] == ans[i] else False}')

print()
print("accuracy: ", kn.score(test_input, test_target))  # 1.0
