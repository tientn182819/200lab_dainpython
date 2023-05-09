import numpy as np

#tranpose tức là chuyển vị, có nghĩa là chuyển vị một ma trận. ví dụ từ (6,2) thành (2,6)

array_ex = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]) #2x9

tranpose_array_ex = np.transpose(array_ex) #9x2

print(tranpose_array_ex)