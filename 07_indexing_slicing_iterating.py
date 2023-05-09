#Indexing, slicing, iterating for 1-D array

import numpy as np

a = np.arange(10)**3

print('array a = ', a)

#index là giá trị biểu thị vị trí của phần tử
print('indexing a[2] = ', a[2])

#slicing là một đoạn các phần tử trong mảng tạo thành mảng con
print('slicing a[2:5] = ', a[2:5])

#với slicing có bước nhảy có dạng a[x:y:z] với x là điểm bắt đầu, y là điểm kết thúc, z là bước nhảy 
print('slicing with step a[:6:2]= ', a[:6:2])

#gán giá trị với slicing: ví dụ muốn gán cho giá trị với slicing thành 1000 ta sẽ sử dụng 
a[:6:2]=1000
print('slicing with step a[:6:2] and element is 1000= ', a)

#Đảo ngược mảng thực chất là việc sử dụng bước nhảy -1 (hoặc -2,...) để đảo ngược mảng 
reversed_a = a[::-1]
print('reversed a is ', reversed_a) 

#Indexing, slicing, iterating for Mul-D array

b = np.array([[1, 2, 3, 0],
              [4, 5, 6, 1],
              [8, 9, 10, 2]]) #array with 3 row 4 column

print('b= ', b)

print('b[2,3] = ', b[2,3]) #2 là index cho hàng, 3 là index cho cột => output = 6

print('b[0:3,1] = ', b[0:3,1]) #=[0,1], [1,1], [2,1] => output = 2,5,9
#nếu mảng là axb thì phải chạy từ 0 đến a+1 hoặc b+1 mới có thể ghép mảng đầy đủ 

#có thể viết cách duyệt bằng cú pháp như sau 
print('b[:,1] = b[0:3,1] = ',b[:,1] )

#duyệt cả hàng cả cột cùng một lúc 
print('b[1:3, :]= ', b[1:3, :])# duyệt tất cả các cột lần lượt với hàng 1,2 => sẽ tạo ra 2 mảng 

print('b[-1]= ', b[-1]) #duyệt hàng cuối cùng, giá trị âm sẽ duyệt giá trị hoặc là từ phải sang hoặc là từ dưới lên