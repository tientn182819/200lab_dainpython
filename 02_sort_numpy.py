import numpy as np

arr = np.array([2,1,3,5,4,7,9,6,8])
ls1 = (1,5,1,4,2)
ls2 = (3,2,5,6,5)

#sort arrays in ascending order
sorted_array = np.sort(arr)
print(sorted_array)
#1,2,3,4,5,6,7,9

#reverse sorted arrays
# về bản chất mảng numpy không thể sort theo kiểu  descending được nên phải sort theo kiểu ascending sau đó reverse hàm
reverse_array = sorted_array[::-1]
print(reverse_array)

#np.argsort() 
#argshort sẽ sắp xếp các phần tử theo thứ tự bé đến lớn sau đó đưa ra vị trí index của những phần tử theo thứ tự đó
argsort_array = np.argsort(arr)
print(argsort_array)

#np.lexsort
#hàm tạo 2 mảng thành 1 mảng 2 phần tử theo trục dọc sau đó xếp chúng theo giá trị vd (1,0) <(1,1) sau đó in ra index của từng mảng nhỏ
lexsort_array = np.lexsort((ls1,ls2)) #như này thì sẽ xếp theo ls2 tức là (3,1) (2,5) ...
print(lexsort_array)
#output = 1,0,2,4,3

