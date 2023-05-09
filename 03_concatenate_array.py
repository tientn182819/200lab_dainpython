import numpy as np

# phải nối mảng có cùng số chiều 
# a = np.array([1,2,3,4,5])
# b = np.array([2,3,8,9,10])

x = np.array([[1, 2],[3, 4]])
y = np.array([[3, 4],[5, 6]])

# concatenate_array = np.concatenate((a,b))
# print(concatenate_array)


concatenate_array1 = np.concatenate((x,y), axis = 0)
# #axis để hàm hiểu nối theo dạng gì, =0 tức là nối thành hàng
# #output = [1,2], [3,4], [3,4], [5,6]
concatenate_array2 = np.concatenate((x,y), axis = 1)
# #nối 2 hàng thành một cột
# #output = [1,2,3,4], [3,4,5,6]
print(concatenate_array1)
print(concatenate_array2)

