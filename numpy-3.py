import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go


a=np.linspace(-10,9,20)
b=np.linspace(-10,9,20)

xx,yy=np.meshgrid(a,b)

#plt.scatter(xx,yy)

def func(x,y):
    return x**2+y**2
zz=func(xx,yy)

fig =px.scatter_3d()
fig.add_trace(go.Surface(x=xx,y=yy,z=zz))

#fig.show()
#plt.show(block=True)

###SOME IMPORTANT FUNCTION OF NUMPY 
#https://www.google.com/url?q=https%3A%2F%2Fnumpy.org%2Fdoc%2Fstable%2Freference%2Fgenerated%2Fnumpy.sort.html
#this is the which have all the important functions of numpy

##sort
#this is the function used to sort the numpy array 
#in this sort function we can choose the sorting algo by kind='mergesort' etc.

#1d array 
a=np.random.randint(10,50,15)

print(np.sort(a))#to sort in ascending order
print(np.sort(a)[::-1])#to sort in descending order

#2d array 
b=np.random.randint(10,50,24).reshape(6,4)

print(np.sort(b))#this is sort row-wise
print(np.sort(b,axis=0))#to sort column-wise

##append
#it appends the value to the array 

#1d array 
print(np.append(a,500))

#2d array 

print(np.append(b,np.ones((b.shape[0],1)),axis=1))
#to add ones at the last of column 

##concatenate
#this function is add the existing array row-wise/column-wise

c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)

print(np.concatenate((c,d),axis=0))
#this is to concatenate row-wise

print(np.concatenate((c,d),axis=1))
#this is to concatenate column-wise

##unique
##with the help of np.unique(), we can get the unique values from an array given as parameter in np.unique() method

e=np.array([1,2,2,2,3,3,3,1,4,5,5,4])

print(np.unique(e))#to get the unique element from the array

##expand_dims
#with the help of Numpy.expand_dims() method,we can get the expanded dimesion of an array 
#with the help of it we can convert oneD to 2d 

a=np.random.randint(10,50,15)
new=np.expand_dims(a,axis=0)#to expand the 1d to 2d ,, row-wise
#we can also check the dimesion by using new.shape() 

##np.where()//not giving desired output in vscode
#The np.where() function refers the indices(index) of elements in an input array where the given condition is satisfied.
#np.where(condition,true,false) if condition satisfied then true will be executed otherwise false

#find all the indices with value greater than 50.
a=np.random.randint(10,100,15)
res=np.where(a>50)
print(res)

#replace all the values >50 with 0
res1=np.where(a>50,0,a)
print(res1)

##np.argmax()
#it returns the index of maximum element of array in particular axis.

print(np.argmax(a))
#we can also check the index of maximum element ,, row-wise/column-wise
b=np.random.randint(10,50,24).reshape(4,6)
print(np.argmax(b,axis=0))#for column-wise
print(np.argmax(b,axis=1))#for row-wise

##np.argmin()
#it returns the index of minimum element of array in particular axis.
#it's functionality is same as argmax()
np.argmin(a)

##np.cumsum
#this function is used when we want to compute the cummulative sum of array     elements over a given axis.

print(np.cumsum(a))#1d array

#2d array 
#if we donot specify the axis then it will convert it into 1d array then perform the operation.

print(np.cumsum(b))

print(np.cumsum(b,axis=0))#for column-wise

##np.cumprod
#it is used to find the cumulative product 
print(np.cumprod(a))


##np.percentile
#this function is used to find the percentile of the given data along the specified axis.

print(np.percentile(a,50))#to get the percentile 

##np.histogram()
#it represents the frequency of data distribution 
a=np.random.randint(0,100,50)
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))#bins represent the range in which we want the frequency of data 

##np.corroef
#it returns Pearson product-moment correlation coefficients.

salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))

##np.isin()
#with this function,we can see that one array having values are checked in a different numpy array having different elements with different sizes.

items=[10,20,30,40,50,60,70,80,90,100]

print(a[np.isin(a,items)])#it checks whether the given items are in a or not.
#it can search multiple items at a time

##np.flip()
#it reverses the order of array elements along the specified axis,preserving the shape of array.

print(np.flip(a))#it's like producing the mirror image of array 

#same with 2d array ,, it flips the array row-wise and column-wise both 
print(np.flip(b))
#to flip the 2d array , only column-wise
print(np.flip(b,axis=0))

##np.put(it is permanent operation/handle with care)
#this function replaces the specific elements of an array with given values of p_array.Array indexed works on flattened array.

print(np.put(a,[0,1],[540,108]))#np.put(desired_array,position_where_changes_needed,changes)

##np.delete
#it is used to delete multiple array items at a time using it index values.

print(np.delete(a,[0,2,3]))

###Set functions 

##np.union1d
m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])

print(np.union1d(m,n))#it gives union of m and n

##np.intersect1d
print(np.intersect1d(m,n))#it gives intersection of m and n

##np.setdiff1d
print(np.setdiff1d(m,n))#it gives the difference of m and  n

##np.setxor1d
print(np.setxor1d(m,n))#it gives the xor of m and n

##np.in1d
#it checks whether the given item is present in given array or not
print(np.in1d(m,1))


##np.clip()
#it is used to clip(limit) the values in an array.
#it is usually used when we need the elements in range 

print(np.clip(a,a_min=25,a_max=75))#it gives number in range of 25 and 75


vjhbjh