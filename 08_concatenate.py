import numpy as np 

x = np.array([1,2,3])
y = np.array([[99],[99]])
z = np.arange(9.0) # tạo một mảng 9 phần tử bắt đầu từ 0
grid = np.array([[9,8,7],[9,8,7]])

#vì concatenates chỉ sử dụng được khi các mảng có size giống nhau, vì vậy nếu size khác nhau mình sẽ phải dùng một số hàm dưới đây 

np_vstack = np.vstack([x, grid]) #vstack aka vertical stack cho phép chồng các hàng của mảng này lên mảng kia với điều kiện các mảng phải cùng số cột
print('np.vstack = ', np_vstack)

np_hstack = np.hstack([y, grid])#hstack aka honrizontal stacktương tự vstack nhưng ghép theo phương ngnag
print('np.hstack = ', np_hstack)

#Split of arrays in Numpy 
# TYPE 1
np_split1 = np.split(z,3) 
#np.split(a,b) - a là mảng cần chia, b là số phần mình muốn chi mảng thành. Lưu ý là số phần tử của a phải chia hết cho b
print(np_split1)

# TYPE 2
np_split2 = np.split(z, [2,4,6,9,11])
#z là số phần tử, ở đây sẽ in ra 4 mảng. mảng 1 là số phần tử từ index 0 đến index 2. mảng 2 là sô phần tử từ index 3 đến index 4. Cứ thế...
# nếu nhập vào giá trị quá index của mảng thì những mảng sau sẽ in ra mảng rỗng
print(np_split2)