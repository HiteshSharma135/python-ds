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
#with the help of np.unique(), we can get the unique values from an array given as parameter in np.unique() method

e=np.array([1,2,2,2,3,3,3,1,4,5,5,4])

print(np.unique(e))#to get the unique element from the array




