import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y=x**2
#plt.plot(x,y)
#plt.show(block=True)

###Numpy array vs python list

##speed
#time taken by python list
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
import time

start=time.time()#it calculate current time
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)#it calculate difference of current time and starting time... 

#time taken by numpy array
import numpy as np
a=np.arange(10000000)
b=np.arange(10000000,20000000)

start=time.time()
c=a+b
print(time.time()-start)

#by these we can understand that numpy array is faster than python list

##memory
#memory taken by list
a=[i for i in range(10000000)]

import sys

size=sys.getsizeof(a)#this function is used to calculate the memory taken by list a

print(size)

#memory taken by numpy array
b=np.arange(10000000)
size1=sys.getsizeof(b)#we can also specify the datatype of integer we want to use as,, if we want to store smaller numbers ,, we can use dtype=int32,int16 in numpy array

print(size1)    

##convenience
#numpy array is more convinient to use than python list


###ADVANCE INDEXING

##fancy indexing
a=np.arange(24).reshape(6,4)

#if we want to access the first,third ,four ,last row of nd array

print(a[[0,2,3,5]])

#accessing first,third and last column
print(a[:,[0,2,3]])#here we use : because we need entire row of selected column

##Boolean indexing
#it is used whenever we need to access the item based on different conditions

b=np.random.randint(1,100,24).reshape(6,4)
#here random is a function of np which creates random number,, randomint is associated with random to create random integer values(it takes intialvalue,final value,number of values we want)

#find all the numbers greater than 50

b>50#if we directly do that it will give boolean values, to mask them into integer values we use b[b>50] now we get the integer values which are greater than 50

print(b[b>50])

#to find out even numbers
print(b[b%2==0])

#all numbers greater than 50 and even

print(b[(b>50) & (b%2==0)])
#here we are using &(bitwise and) not and(logical and) #because comparision between the array items gives us the boolean values that's why we #use bitwise and

#find all the numbers that are not divisible by 7
print(b[~(b%7==0)])


###BROADCASTING
#The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

#The smaller array is “broadcast” across the larger array so that they have compatible shapes

###Broadcasting Rules
#1. Make the two arrays have the same number of dimensions.
#If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.

#2. Make each dimension of the two arrays the same size.

#If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
#If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised


##same shape
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)

print(a+b)#we can add the arrays having same shape

##different shape












