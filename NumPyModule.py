import numpy

a = numpy.arange(15).reshape(3, 5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]


b = numpy.arange(0,30,2).reshape(3,5)
print(b)
# [[ 0  2  4  6  8]
#  [10 12 14 16 18]
#  [20 22 24 26 28]]


c = numpy.arange(0,30,2).reshape(3,5,1) #3rd dimentional
print(c)
# [[[ 0]
#   [ 2]
#   [ 4]
#   [ 6]
#   [ 8]]

#  [[10]
#   [12]
#   [14]
#   [16]
#   [18]]

#  [[20]
#   [22]
#   [24]
#   [26]
#   [28]]]


#we have here two examples of arrays, but with same size and different elements

#arange(), this function is like a range used in a loop, but here with those range of numbers, we create elements for the array
#reshape(), it let us make a new shape to the array, to let it have new dimensions and shape

print(a.shape) # we can see the shapes of an array
# (3, 5)
print(b.size) # we can see the total size of it
# 15


#another way of an array creation:
d = numpy.array([1,2,3])
e = numpy.array([1.5,2.5,3.5])

print(d)
# [1 2 3]

print(e)
# [1.5 2.5 3.5]

print(d.dtype)
# int32

print(e.dtype)
# float64


f = numpy.array([1,2,3], dtype=float)
print(f)
# [1. 2. 3.]


# how to create the null array
g = numpy.zeros((2,3)) #inside we have to put as arguments the shapes of the matrix
print(g)
# [[0. 0. 0.]
#  [0. 0. 0.]]

#and well, what are the operations :? , now we will show some examples of them :D

#addition
h = a+b
print(h)
# [[ 0  3  6  9 12]
#  [15 18 21 24 27]
#  [30 33 36 39 42]]

#sustraction
i = a-b
print(i)
# [[  0  -1  -2  -3  -4]
#  [ -5  -6  -7  -8  -9]
#  [-10 -11 -12 -13 -14]]


#elementwise product
j = a*b
print(j)
# [[  0   2   8  18  32]
#  [ 50  72  98 128 162]
#  [200 242 288 338 392]]

#matrix product
k = numpy.arange(2,17,1).reshape(5,3)
j = a @ k
# another option of writting this would be : j = a.dot(k), and both of them give us the same result
print(j)
# [[110 120 130]
#  [310 345 380]
#  [510 570 630]]
