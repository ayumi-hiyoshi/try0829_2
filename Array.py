import numpy as np

# 適当な1次元配列を作成
arr1 = np.array([1, 2, 3, 4, 5])
print("1次元配列:", arr1)

# 適当な2次元配列を作成
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2次元配列:")
print(arr2)

# 0から9までの連番配列
arr3 = np.arange(10)
print("連番配列:", arr3)

# 3x3のランダムな配列
arr4 = np.random.rand(3, 3)
print("ランダム配列:")
print(arr4)

# 配列の形状を確認
print("arr2の形状:", arr2.shape)
print("arr2の合計:", arr2.sum())
