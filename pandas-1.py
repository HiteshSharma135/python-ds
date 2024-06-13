##Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

###Pandas Series
#A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.

## A series have index and its value 

##importing pandas
import numpy as np
import pandas as pd

###CREATING SERIES

##Creating series using list

#string
country=['India','Srilanka','USA','Nepal']
print(pd.Series(country))
#in pandas string=objects

#integer
runs=[12,25,28,77,88,45]
print(pd.Series(runs))

#custom index
#it is used when we want to customize the index values (initially it starts with zero)

marks=[85,78,69,78,89]
subjects=['hindi','english','maths','science','sst']

print(pd.Series(marks,index=subjects))

#setting a name
#it is used to provide a name to the series

print(pd.Series(marks,index=subjects,name='Hitesh marks'))


##Creating series using dictionaries

marks={
    'maths':85,
    'hindi':78,
    'english':74,
    'science':89
}
marks_series=pd.Series(marks,name='marks of student')
print(pd.Series(marks,name='marks of student'))

##Series Attributes

#size
#it tells the items present in series

print(pd.Series(marks).size)

#dtype
#to know the datatype of items in series
print(marks_series.dtype)

#name
#it tells the name of the series object

print(marks_series.name)

#is_unique
#it tells whether every item of series is unique or not.. it returns boolean value.
#true==> every item is unique

print(marks_series.is_unique)

new=pd.Series([1,1,2,2,23,4]).is_unique
print(new)

#index
#it gives the index of series

print(marks_series.index)

#values
#it gives the value of series
#it returns a numpy array

print(marks_series.values)

##Series using read_csv

#with one col
#pd.read_csv('subs.csv')

##pd.read_csv whenever get the data it get into dataframe object now if we want to explicitly change it behaviour to series
#write pd.read_csv('subs.csv',squeeze=True)

#pd.read_csv('subs.csv',squeeze=True)
#this feature was used in older version of python now it is not used

subs=pd.read_csv('subs.csv')

#with 2 col

vk=pd.read_csv('kohli_ipl.csv',index_col='match_no')
#in 2 col we need to specify the index col value
print(vk)

movie=pd.read_csv('bollywood.csv',index_col='movie')
print(movie)


###Series Methods

##head and tail
#head is  used to give the preview of data
#by default itp gives top 5 rows of data
print(subs.head())

#if we want to only 3 top rows
print(vk.head(3))

#tail fetch the last five rows
print(vk.tail())

#if we want to fetch the data of last 10 matches
print(vk.tail(10))

##sample
#it randomly provides the data of one row 
print(movie.sample())

#if we want randomly 5 movies
print(movie.sample(5))

##value_counts
#it is used to frequency of data occurence 

#in our case:- find the which actor has made how many movies
print(movie.value_counts())#descending order

##sort_values(it make only temporary changes)
#it is  used to sort the values in ascending order

print(vk.sort_values(by='runs'))

print(vk.sort_values(by='runs',ascending=False))#to sort in descending order

#to get the most runs by vk in 5 matches

print(vk.sort_values(by='runs',ascending=False).head())

#to get the most run in a match
print(vk.sort_values(by='runs',ascending=False).head(1).values[0])
#to only the get the runs we use the values[0]

#NOTE:- to make the permanent changes in data use sort_values(inplace=True)

##sort_index
#it is used to sort the index of data

print(movie.sort_index())#it will sort the  movies by their names in ascending order

#here also there inplace parameter which can be used to make the permanent changes in dat


###SERIES MATHS METHODS

##count
#it is same as size there is difference is that (size counts the nan values but count doesnot)

print(vk.count())

##sums
#to count the sum 
print(subs.sum())

##prod
#to count the product 
print(vk.prod())

##mean/mode/median/std/var

print(subs.mean())
print(vk.median())
print(movie.mode())
print(subs.std())
print(vk.var())

##min/max
print(subs.min())

print(subs.max())

##describe
#it provides the summary of given data
print(vk.describe())

###SERIES INDEXING

##integer indexing
x=pd.Series([11,12,13,45,15,78,56])
print(x[2])#to get the numbers by index

##negative indexing
#it doesnot work on series

##