import numpy as np 

array = np.arange(16.0)

#Split of arrays in Numpy 
# TYPE 1
np_split1 = np.split(array,4) 
#np.split(a,b) - a là mảng cần chia, b là số phần mình muốn chi mảng thành. Lưu ý là số phần tử của a phải chia hết cho b
print(np_split1)

# TYPE 2
np_split2 = np.split(array, [2,4,6,9,11,16])
#z là số phần tử, ở đây sẽ in ra 4 mảng. mảng 1 là số phần tử từ index 0 đến index 2. mảng 2 là sô phần tử từ index 3 đến index 4. Cứ thế...
# nếu nhập vào giá trị quá index của mảng thì những mảng sau sẽ in ra mảng rỗng
print(np_split2)

print(array)
array_4 = np.arange(16.0).reshape(4,4)
print("array_4=", array_4)
#np.hsplit() - horizontal split
# Mảng sẽ được tạo dựng thành ma trận thành a hàng x b cột. với tham số truyền vào sao cho số cột phải chia hết cho số đó. sẽ coi như là những đường thằng cắt chia ma trận thành các phần bằng nhau. như ở vdu dưới đây với ma trận 4x4 mà dùng hspilt(x,2) tức là chia làm 2 phần thì ta sẽ chia dọc ma trận thành hai phần bằng nhau. 
hsplit1 = np.hsplit(array_4,2)
print("hsplit1= ", hsplit1)

#nếu muốn cắt những phần khác nhau trong mảng ta dùng hàm như sau 
hsplit2 = np.hsplit(array_4, np.array([3,6])) 
# với mảng array_4 ta chia làm 3 phần, phần 1 từ index 0 đến index 3, phần 2 từ index 4 đến index 6, phần 3 từ index 7 đổ đi 
#chúng ta lại tưởng tượng lại ma trận sau đó kẻ một đường dọc phân chia, như bài này ta đặt đường thẳng sau phần tử thứ 3 sau đó kẻ dọc, vì vậy mảng 1 mới là 12 phần tử tước phần kẻ dọc, mảng 2 mới là 4 phần tử còn lại, mảng 3 mới là mảng rỗng. Đáp án như dưới 
print("hsplit2 = ", hsplit2)


#.vsplit() có 2 TH hoàn toàn tương tự như hsplit như theo hàng ngang 
vsplit1 = np.vsplit(array_4,2)
vsplit2 = np.vsplit(array_4,[3,6])
print("vsplit1 = ", vsplit1)
print("vsplit2 = ", vsplit2)



