###What is numpy?

#NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

#At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types

###Numpy Arrays Vs Python Sequences
#NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

#The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

#NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

#A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.

###CREATING NUMPY ARRAYS

## np.array(1D)
import numpy as np

#numpy array just take list as input
a = np.array([1,2,3])
print(a)

##2D AND 3D

b = np.array([[1,2,3],[4,5,6]])
print(b)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

## dtype
##if we want the data should be of float type than we can use dtype
np.array([1,2,3],dtype=float)

## np.arange
#it is also a way to create a numpy array ,,, it takes range for ex:-(1,11) and then print the array from 1 to 10 (excludes last value)
np.arange(1,11)

np.arange(1,11,2)#to take an array with alternate numbers

## with reshape
#it change the shape of an array like (it can change the 1d to 2d array and many more dimensions ... 3d,4d...)

np.arange(10).reshape(2,5)#it will print the array from 0 to 9 in 2d 

np.arange(16).reshape(2,2,2,2)
#it will create a 4d array from 0 to 15

## np.ones and np.zeros

#it will help in creating on the go array having all the elements as 1 or 0 
#it takes value in tuples which defines its dimension in arrays 
#it can be helped in initializing arrays
np.ones((3,4))

np.zeros((3,4))
#it is same as np.one , it is also use in creating array having all the element as 0

## np.random

#it is used to create an array having random values from 0 to 1 (same as np.ones/np.zeroes)
np.random.random((3,4))

## np.linspace

#it is also used to create an array , it input as (initial value,final value, number of values we want in array)
#np.linspace-> linearspace (it creates a linear space between the points)
#for ex:- if we want 10 numbers between -10 and 10 then it will 10 numbers at equal distance
#here also dtype is use to specify the type of data 
np.linspace(-10,10,10,dtype=int)

## np.identity

#it is used to create an identity matrix
#it takes number as input which specify its dimension
np.identity(3)


###ARRAY ATTRIBUTES

a1 = np.arange(10,dtype=np.int32)#here dtype=np.int32 is used to specify the size of int is 4byte which is bydefault 8 bytes in google collab
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

## ndim
#it is used to get the number of dimension of an array 
a3.ndim

## shape
#it will tell about the number of rows and columns 
print(a3.shape)
a3

## size
#to get the number of elements in an array
print(a2.size)
a2

## itemsize
#it specifies how much memory is being used by an array
a3.itemsize

## dtype
#to get the datatype of a array 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


###CHANGING DATATYPE

## astype
#it is used to change the datatype 
a3.astype(np.int32)


###ARRAY OPERATIONS

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

## scalar operations

# arithmetic
#it is an arithmetic operation like +,-,*,/,**
#every arithmetic operation will work on the array and it makes the operation done with every element of array like a1*2 it will multiply 2 with every element of array
print(a1 ** 2)

## relational
#relational operator like ==,>,<,<=,>=,!= every operator works and it will compare it with each element of an array and return boolean values  
a2 == 15

## vector operations(operations which work on 2 numpy arrays)

# arithmetic
a1 ** a2


###ARRAY FUNCTIONS

a1 = np.random.random((3,3))
a1 = np.round(a1*100)

## max/min/sum/prod

#these functions are used to 
#max-> to get the maximum number out of array
#min->to get the minimum number out of array
#sum->to get the sum of all elememts of array
#prod-> to get the product of all elements of array

#in case we need the column and row specify element(that means if we want the maximum or minimum element from a particular row or column)
## 0 -> col and 1 -> row
# use np.max(a1,axis=0)#here a1-> array,axis determine either row or column
np.prod(a1,axis=0)


## mean/median/std/var

#(here also we have the flexibility of using it on particular row or col)
##mean-> it calculates the mean of array
##median-> it calculates the median of array
##std->to calculate the standard devaiton 
##var->to calculate the variance 

np.var(a1,axis=1)

## trigonomoetric functions

#here we can use any trigonometric function that is(sin,cos,tan etc...)
np.sin(a1)#it calculates the sin value for every element of array

## dot product
#condition to be match before dot product is that column of first array and row of second array should match

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

np.dot(a2,a3)

## log and exponents
#these function are used to calculate the logarithmic and exponential value of elements of array

np.exp(a1)

## round/floor/ceil

np.ceil(np.random.random((2,3))*100)


###INDEXING AND SLICING

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

##Indexing(it is the way of accessing the elements of array using index)

#to access 1d array
a1[2]

#to access 2d array
a2[1,0]#it takes input as row number and column number which specify the element(indexing starts from 0)

#to access 3d array 

#as we know 3d is combination of 2 2d array so to access the element of 3d array first we need to tell in which 2d array elememt we want ,, after that row number then column number

a3[0,1,2]


##Slicing 
#in indexing we are accessing only one element at a time but with help of slicing we can access multiple elements at a time

#1d array (it is same as we study in string and list)

a1[2:5]#last number not included

a1[2:5:2]#to get the alternate element

a1[2:]#to access every element till last


#2d array 

#if we want only first row 
a2[0,:]#0-> row and :-> all column of first row

#if we want third column
a2[:,2]#:-> every row of third column ,2-> third column

### for more on slicing concept 
###Watch session 13 on Numpy fundamentals from campusx 

###Iterating

#loop in 1d
for i in a1:
    print(i)
#it will print all the elements of 1d array 

##loop in 2d 

for i in a2:
    print(i)
#it will print the elements in array form 

#loop in 3d

for i in a3:
    print(i)

#it will print the elements in 2d array format

#if we want to access all the elements of 3d array there is a function nditer
for i in np.nditer(a3):
    print(i)

#np.nditer() to access all the elements of 3d array or nd array 


###Reshaping

##transpose
#it change the row -> column and column-> row

np.transpose(a2)
#second syntax
a2.T

##ravel(it will transform nd array to 1d array )

a2.ravel()

###Stacking
#it means to add two array in horizontal or vertical type

##horizontal stacking
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)

#to stack them in horizontal manner
np.hstack((a4,a5))

##vertical stacking
np.vsta((a4,a5))

###Splitting
#it is opposite of stacking

#horizontal splitting

np.hsplit(a4,2)#here 2 specify in how many we want to split the array

##vertical splitting

np.vsplit(a4,4)
