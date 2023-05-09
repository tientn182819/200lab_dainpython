import numpy as np 

''' Nhiều quá nên từ khóa GG để tìm là aggregation'''
'''demo như ở dưới đây'''

array1 = np.arange(4)
#Cách 1:
print("min(array1)", np.min(array1))
print("max(array1)", np.max(array1))

#Cách 2:
print("array1.min = ", array1.min())
print("array1.max = ", array1.max())


'''Đối với mảng nhiều chiều ta ví dụ như sau '''

M = np.random.randint(3,4)
print('M:',M)

print('M.sum() =', M.sum() ) #Chỉ là cộng tất cả các giá trị bằng 0 lại bình thường 
print('M.min(axis=0)=', M.min(axis=0)) # lúc này mảng trả về một mảng có 4 phần tử, mỗi phần tử là số nhỏ nhất của từng cột trong mảng cũ
print('M.min(axis=0)=', M.min(axis=1)) # tương tự nhưng áp dụng theo hàng, tức là mảng trả về sẽ chỉ bao gồm có 3 phần tử.