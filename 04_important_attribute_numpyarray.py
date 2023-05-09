import numpy as np

array_ex = np.array([[[1,2,3,4],[5,6,7,8]],
                     [[1,2,3,4],[5,6,7,8]],
                     [[1,2,3,4],[5,6,7,8]]])


#ndarray.ndim cho biết số chiều của mảng truyền vào là bao nhiêu (dimension)
print('So chieu cua mang truyen vao la: ', array_ex.ndim)
#output: 3

#ndarray.size cho biết tổng số phần tử có mặt trong bảng
print('Tong so phan tu co trong mang la: ', array_ex.size)
#output: 24

#ndarray.shape cho biết hình dáng của các phần tử trong mảng như thế nào 
#VD: mảng trên là mảng 3 chiều, mỗi chiều có 2 phần tử mỗi phần tử 4 giá trị 
print('Hinh dang cua mang nay la: ', array_ex.shape)

#ndarray.dtype cho biết kiểu dữ liệu đang lưu trữ ở trong mảng là gì:
print('Kieu du lieu cua cac phan tu co trong mang la: ', array_ex.dtype)

#ndarray.itemsize cho biết mỗi phần tử trong mảng có giá trị là bao nhiêu bytes
print('Moi phan tu trong mang bao gom ', array_ex.itemsize,' byte')
