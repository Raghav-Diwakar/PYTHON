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

print("\nIndexing in numpy\n")
print(b[3]) 
print(c[1,1])
print(d[1,1,2])
print("\n")

print("\nSlicing of array\n")
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
print("\nCopy array is ",acva)
# view array changed on changing base array
print("\nView array is ",acvb)


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

print("\nArray reshape in 2-D(4,4)\n",reshapea)
print("\nArray reshape in 3-D(2,2,3)\n",reshapeb)

# at any one unknown place you can pass -1 
# numpy calculate accordingly

print("\nArray reshape in 3-D(-1,2,2)\n",reshapec)


# Interating array 

ia = np.array(12)
ib = np.array([1,2,3,4,5])
ic = np.array([[2,4,6],[1,3,5]])
id = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print('\nIterating 1 - D array\n ')
for i in ib :
    print(i)
print('\nIterating 2 - D array , iternal array wise in list like [--] , [--]\n')
for i in ic :
    print(i)
print('\nIterating 2 - D array in sequence\n ')
for i in ic:
    for j in i :
        print(j)
print('\nIterating 3 - D array , iternal array wise in list like [[--],[--]] , [[--][--]]')
for i in id :
    print(i)
print('\nIterating 3 - D array in sequence \n')
for i in id:
    for j in i :
        for z in j:        
            print(z)


# concept of nditer 

# it help  when print N-D array in seqence 
# we can not have to write n for loop in it 
print("\n3-d Array using nditer\n")

ndd = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
for x in np.nditer(ndd):
    print(x)

# concept of op_dtype and flag =['buffered']
# when we have to convert in different data type
# flag = buffered is used because datatype is not change in original so it require extra space

print("\nIterating with different data type\n")
opd = np.array([1,2,3,4,5,6,7,8,9,10])
for i in np.nditer(opd,flags=['buffered'],op_dtypes=['S']):
    print(i)

# Iterating with different step size 
print("\nIterating with different step size\n") 
ss = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(ss[:,::2]):
    print(i)

# Enumerated iteration = means mention sequence number
print("\nEnumerate iteration of 1-D array give in ((sqno,)no)\n")
en = np.array([1,2,3,4,5,6,7,8,9,10])
for i in np.ndenumerate(en):
    print(i)

print("\nEnumerate iteration of 2-D array give in ((sqno,)no)\n")
end = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.ndenumerate(end):
    print(i)


# Join two array

print("\nConcatenation of two string\n")
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
print("\nConcatenate using stack\n")
j3 = np.array([1,2,3,4])
j4 = np.array([5,6,7,8])
j34 = np.stack((j3,j4),axis=1)
print(j34)

#join using hstack
print("\nJoin using hstack\n")
j5 = np.array([1,2,3,4])
j6 = np.array([5,6,7,8])
j56 = np.hstack((j5,j6))
print(j56)

#join using vstack
print("\nJoin using vstack\n")
j7 = np.array([1,2,3,4])
j8 = np.array([5,6,7,8])
j78 = np.vstack((j7,j8))
print(j78)

#join using dstack
print("\nJoin using dstack\n")
d7 = np.array([1,2,3,4])
d8 = np.array([5,6,7,8])
d78 = np.dstack((d7,d8))
print(d78)


# split is opposite of join 
print("\nArray split in three array\n")
spl = np.array([1,2,3,4,5,6,7,8,9,10])
nspl = np.array_split(spl,3)
print(nspl)
print("\nNew array of above are\n")
print(nspl[0])
print(nspl[1])
print(nspl[2])

# we have also method (split()) but array_split will work fine in case of data insufficient in original

# we can also split in 2-D array
print("\n2-D array spliting\n")
two = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
twos = np.array_split(two,3)
print(twos)
print("\n2-D array spliting with axis\n")
twoa = np.array_split(two,3,axis=1)
print(twoa)

# using hsplit() opposite of hstack()
nwoh = np.hsplit(arr,3)
print(nwoh)

# Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().


# Searching technoque
print("\nSearching using wherr()\n")
se = np.array([11,2,3,4,5,6,7,8,9,10,12,13,14,15,16])
x = np.where(se==10)
print(x)

#searchsorted() perform binary sort and search
y = np.searchsorted(se,11)
print(y)

# for inserting element in array 
print("\nFinding position of inserting element\n")
ins = np.searchsorted(arr,[17,1])
print(ins)

# Sorting
print("\nSorting of array\n")
arry = np.array([1,3,5,4,2])
print(np.sort(arry))

#sorting of alphabets, alphabetically accordingly 
alpa = np.array(['banana', 'cherry', 'apple'])
print(np.sort(alpa))

#sort of Boolean elements
#False element comes first and then true 

# sorting of 2-D array internally 
twod = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(twod))


# filtering of array
print("Filtering of array")
opdn = np.array([1,2,3])
nx = [True ,False,True]
nnx = opdn[nx]
print(nnx)


# Example of filtering array
'''
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
'''


