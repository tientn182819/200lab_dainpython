#ufuncs aka universal functions

#CÁCH 1: SỬ DỤNG PYTHON LIST
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1,10,size=5)
compute_reciprocals(values)
print(compute_reciprocals(values))


#CÁCH 2: DÙNG THƯ VIỆN NP
print(1.0 / values) 
# Tức là thay vì việc mình dùng vòng lặp thì numpy đã thiết kế để cho mình thực hiện một lần với cả 1 mảng numpy chứ k tách ra thành từng vòng lặp một

#Ufuncs có hai loại là unary ufuncs tức là mình truyền vào 1 tham số cho hàm, còn Binary ufuncs tức là truyền vào 2 tham số cho hàm.
