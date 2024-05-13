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

import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 데이터 합치기
fish_length = bream_length + smelt_length
fish_weight = bream_weight + smelt_weight
# 데이터 전처리
fish_data = np.column_stack((fish_length, fish_weight))
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
# 타겟 데이터
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)
# 샘플링 편향 제거
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify=fish_target,

                                                                      random_state=42)
# scale => stand scale
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis= 0)
train_scaled = (train_input - mean) / std
test_scaled = (test_input - mean) / std

# 모델 훈련
kn = KNeighborsClassifier(n_neighbors=5) # 이웃(k)의 개수 5개
kn.fit(train_scaled,train_target)
# 모델 평가
print(kn.score(test_scaled,test_target))
# 테스트 데이터 삽입
fish = [25,150]
# scale => stand scale
fish = (fish - mean) /std
print(kn.predict([fish]))

# 산점도 시각화
plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(fish[0],fish[1],marker="^")
plt.xlabel("length")
plt.ylabel("weight")
plt.show()