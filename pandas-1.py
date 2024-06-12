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
