"""LEARNING NUMPY IN PYTHON"""
"""------------------------"""
"""Numpy Array cơ bản"""
#Import thư viện
import numpy as np  

#Numpy Array with all the elements are 0
a = np.zeros(2)
print('np.zeros(2): ', a)

#Numpy Array with all the elements are 1
b = np.ones(3)
print('np.ones(3): ', b)

#Numpy Array with all the elements are random
c = np.empty(5)
print('np.empty(5): ', c)


#Numpy array with the start point, stop point and step
d = np.arange(5) #default start point is 0, step is 1. So the value you add on the syntax is the stop point
print('np.arange(5)', d)

e = np.arange(1,6,3)# 1 is start point, 6 is stop point, 3 is step
print('np.arange(1,6,3)', e)

f = np.linspace(2,8, num=4)#2 is start point, 8 is end point, num=5 is number of element array.
print('np.linspace(2,8, num=4)', f)

#Dtype in numpy array
#The default datetype of the numpy array is float(np.float64). specify which datatype using dtype
g = np.ones(2, dtype=np.int64)
print('np.ones(2):',g,'Type of g: ' ,type(g))


