import numpy as np

#Tạo một mảng bất kỳ sử dụng hàm random
array = np.random.randint(10, size=(3,4))
#randint để random các phần tử có kiểu dữ liệu int
#size(3,4) nghĩa là mảng gồm 3 chiều mỗi chiều có 4 phần tử (3x4)


print(array)

#Đế ép mảng đã cho để hiển thị trên một mặt phẳng ta dùng nparray.ravel()
#Nếu không truyền tham số vào trong ravel thì mặc định hàm sẽ trải dữ liệu theo hàng
#Để trải dữ liệu theo cột ta sẽ truyền vào tham số order='F'
array_ravel_row = array.ravel()
print(array_ravel_row)

array_ravel_column = array.ravel(order='F')
print(array_ravel_column)

#Sau khi trải phẳng mảng ta có thể biến mảng này thành một mảng có kích cỡ khác bằng hàm reshape
array_reshape = array.reshape((6,2)) #6 chiều mỗi chiều 2 phần tử 
print(array_reshape)
