import numpy as np 


#1, np.insert()
'''np.insert(a, b, c, axis=1/0) bao gồm có 4 tham số. a là tên mảng cần thêm phần tử, b là vị trí cần thêm phần tử, c là phần tử cần thêm . Axis là quy cách xác định phần tử được thêm như thế nào'''

'''Nếu như không có axis thì mảng nhiều chiều lúc đầu sẽ bị flatten(trải phẳng) và thêm vào phần tử như bình thường'''

'''nếu axis bằng 1 thì phần tử sẽ được thêm vào vị trí index b của tất cả các hàng trong mảng
   nếu axis bằng 0 thì phần tử sẽ được thêm vào vị trí index b của tất các các cột trong mảng
'''

array = np.array([[1,1],[2,2],[3,3]])
print('array: ', array)

array_insert = np.insert(array, 1, 5)
print("array_insert: ",array_insert)
#output =  [1 5 1 2 2 3 3]

array_insert_axis1 = np.insert(array, 1, 5, axis=1)
print("array_insert_axis1: ",array_insert_axis1)

array_insert_axis0 = np.insert(array, 1, 5, axis=0)
print("array_insert_axis2: ",array_insert_axis0)

array_index_addarray1 = np.insert(array, 1, [5,5], axis=0) # = np.insert(array, 1, 5, axis=0)
print("array_index_addarray1: ",array_index_addarray1)

array_index_addarray2 = np.insert(array, [1], [[1],[2],[3]], axis = 1)
print("array_index_addarray2: ",array_index_addarray2)

#Khi lựa chọn thêm một mảng vào mảng cần phải lựa chọn mảng hợp lý để phù hợp với axis.
# axis = 0 là thêm hàng, =1 là thêm cột


#np.append()
x = np.append([1,2,3],[[4,5,6],[7,8,9]])
print(x)
#Nếu không có tham số axis thì np.append sẽ flatten tất cả các mảng thành 1 hàng sau đó nối các phần tử lại
#=> output = 1,2,3,4,5,6,7,8,9

y = np.append([[1,2,3],[4,5,6]], [[7,8,9]], axis=0)
print(y)
#Với axis bằng 0 và các mảng có cùng số chiều thì append sẽ thêm vào mảng 1 hàng. Tuy nhiên khi viết hàng muốn thêm vào phải viết bằng 2 dấu ngoặc vuông chứ không phải 1 nếu không mảng sẽ báo lỗi 


"""
----------np.delete()---------------
Cấu trúc: np.delete(a,b,c)
          - a là tên mảng 
          - b là vị trí index cần xóa phần tử
          - c là axis =0/1/none
"""
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

arr_delete1 = np.delete(arr,1,0)
# Với axis = 0 tức là theo hàng. Hàm sẽ xóa đi vị trí index 1 tức là hàng thứ 2 từ trên xuống 
print("arr_delete1= ",arr_delete1)

arr_delete2 = np.delete(arr,1,1)
#Với axis = 1 tức là theo cột, hàm sẽ xóa đi vị trí index 1 tức là cột thứ 2 từ trái sang
print("arr_delete2 = ", arr_delete2)

arr_delete3 = np.delete(arr, [1,3,5], None)
# Với axis = none hàm sẽ flatten mảng ban đầu thành 1 hàng sau đó xóa các phần tử ở index 1,3,5
print("arr_delete3 = ", arr_delete3)