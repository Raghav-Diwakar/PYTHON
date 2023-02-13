import numpy as np 

arr = np.array([1,2,3,4,5,6])
print("Printing 1-D array and its type\n")
print(arr)
print(type(arr))

#  0 - D , 1 - D , 2 - D , 3 - D Array 

a = np.array(12)
b = np.array([1,2,3,4,5])
c = np.array([[2,4,6],[1,3,5]])
d = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print("\n")

print("Dimension of array\n")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print("\n")

# Indexing also possible in numpy
print("Indexing in numpy\n")
print(b[3]) 
print(c[1,1])
print(d[1,1,2])
print("\n")

print("Slicing of array\n")
print(d[0:2,0:2,2])
print("\n")

print("Data Types Of Numpy\n")
print("String , int , float , complex , bool ")

"""
integer = i 
unsigned integer = u  =>  non negative integer
float = f 
string = S
Unicode String = U => like (\u0067\u0066\u0067)
complex float = c 
boolean = b
fixed chunk of memory for other type ( void ) = V
m - timedelta
M - datetime
O - object
"""


