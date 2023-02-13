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

print("Data Types Of Numpy is written in comment below\n")
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


#  Concept of copy and view 

acv = np.array([1,2,3,4,5,6,7,8])
acva = acv.copy()
acvb = acv.view()

acv[0]=100
# Copy array not change on changing base array
print("Copy array is ",acva)
# view array changed on changing base array
print("View array is ",acvb)


# .base concept

base = np.array([11,2,22,3,33])
basea = base.copy()
baseb = base.view()

print(basea.base) # copy array return None
print(baseb.base) # view array return Original array

# shape of array 
# shape return in tuple form 

shapea = np.array(12)
shapeb = np.array([1,2,3,4,5])
shapec = np.array([[2,4,6],[1,3,5]])
shaped = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])

print(shapea.shape)  # 0-D array return ()
print(shapeb.shape)  # 1-D array return (5,)
print(shapec.shape)  # 2-D array return (2, 3)
print(shaped.shape)  # 3-D array return (2, 2, 3)


# Reshape array 

reshape = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
reshapea = reshape.reshape(4,4)
reshapeb = reshape.reshape(2,2,4)
reshapec = reshape.reshape(-1,2,2)


# in reshape .base return original array

print("Array reshape in 2-D(4,4)\n",reshapea)
print("Array reshape in 3-D(2,2,3)\n",reshapeb)

# at any one unknown place you can pass -1 
# numpy calculate accordingly

print("Array reshape in 3-D(-1,2,2)\n",reshapec)


# Interating array 

ia = np.array(12)
ib = np.array([1,2,3,4,5])
ic = np.array([[2,4,6],[1,3,5]])
id = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print('Iterating 1 - D array ')
for i in ib :
    print(i)
print('Iterating 2 - D array , iternal array wise in list like [--] , [--]')
for i in ic :
    print(i)
print('Iterating 2 - D array in sequence ')
for i in ic:
    for j in i :
        print(j)
print('Iterating 3 - D array , iternal array wise in list like [[--],[--]] , [[--][--]]')
for i in id :
    print(i)
print('Iterating 3 - D array in sequence ')
for i in id:
    for j in i :
        for z in j:        
            print(z)


# concept of nditer 

# it help  when print N-D array in seqence 
# we can not have to write n for loop in it 
print("3-d Array using nditer\n")

ndd = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
for x in np.nditer(ndd):
    print(x)

# concept of op_dtype and flag =['buffered']
# when we have to convert in different data type
# flag = buffered is used because datatype is not change in original so it require extra space

print("Iterating with different data type")
opd = np.array([1,2,3,4,5,6,7,8,9,10])
for i in np.nditer(opd,flags=['buffered'],op_dtypes=['S']):
    print(i)

# Iterating with different step size 
print("Iterating with different step size") 
ss = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(ss[:,::2]):
    print(i)

# Enumerated iteration = means mention sequence number
print("Enumerate iteration of 1-D array give in ((sqno,)no)")
en = np.array([1,2,3,4,5,6,7,8,9,10])
for i in np.ndenumerate(en):
    print(i)

print("Enumerate iteration of 2-D array give in ((sqno,)no)")
end = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.ndenumerate(end):
    print(i)


# Join two array

print("Concatenation of two string")
j1 = np.array([1, 2, 3])
j2 = np.array([4, 5, 6])
# if axis is not given it will consider as 0 
jnew =  np.concatenate((j1,j2))
print(jnew)

jar1 = np.array([[1, 2], [3, 4]])
jar2 = np.array([[5, 6], [7, 8]])
#axis = 1 perform concatenate first array of both first and then other 
jn = np.concatenate((jar1,jar2),axis=1)

#join using stack

# stack use axis =1 in two 1-D array 
print("Concatenate using stack")
j3 = np.array([1,2,3,4])
j4 = np.array([5,6,7,8])
j34 = np.stack((j3,j4),axis=1)
print(j34)

#join using hstack
print("Join using hstack")
j5 = np.array([1,2,3,4])
j6 = np.array([5,6,7,8])
j56 = np.hstack((j5,j6))
print(j56)

#join using vstack
print("Join using vstack")
j7 = np.array([1,2,3,4])
j8 = np.array([5,6,7,8])
j78 = np.vstack((j7,j8))
print(j78)

#join using dstack
print("Join using dstack")
d7 = np.array([1,2,3,4])
d8 = np.array([5,6,7,8])
d78 = np.dstack((d7,d8))
print(d78)


