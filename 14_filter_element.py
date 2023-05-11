import numpy as np 

#Dùng để filter phần tử từ mảng a theo mảng b với mảng b thường là boolean element

a = np.array([41,42,43,44,45])
b = [True,False,True,False, True]

print(a[b])

print(a[a<43]) # Tức là để lọc phần tử <43. Ở đây sử dụng ufuncs vì không sử dụng vòng lặp.

print(a[(a<43)&(a>5)]) # Lọc theo nhiều điều kiện

'''np.where(a,b,c)
   a là điều kiện (logical condition)
   b là kết quả trả ra khi điều kiện đúng
   c là kết quả trả ra khi điều kiện sai
'''

c = np.where(a<44, a, a*10)
print(c)

# Một ví dụ căng cực hơn về multidimension
d = np.where([[True, False],[True,False]],[[1,2],[3,4]],[[9,8],[7,6]])

'''
ở đây hàm sẽ so sánh từng giá trị của  vị trí các mảng với nhau. Kết quả trả ra đương nhiên sẽ là một mảng 2x2.
Ở lượt đầu tiên True false true false sẽ tương ứng với 1 2 3 4 theo kiểu như sau 
true  false   =>>>>>>>>>>>>>     1   2
true  true                       3   4
dĩ nhiên 2 giá trị 2 và 4 là false sẽ không hiển thị mà nhận giá trị 1 3 và XẾP THEO CHIỀU DỌC NHƯ CŨ
tương tự như vậy với giá trị 

'''

