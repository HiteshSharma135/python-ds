                   ### PANDAS DATAFRAME ##

##A DataFrame in pandas is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet or a SQL table, or a dictionary of Series objects.

#Key Features of DataFrame
#Two-Dimensional: Data is arranged in rows and columns.
#Size-Mutable: You can insert and delete rows and columns.
#Labeled Axes: Both rows and columns have labels. Rows are indexed by labels (which are often integers) and columns are named.
#Heterogeneous Data: Columns can contain data of different types (e.g., integer, float, string)

import numpy as np
import pandas as pd

###CREATING DATAFRAMES

##Using lists

student_data=[
    [100,80,10],
    [120,90,12],
    [80,50,6],
    [90,80,8]
]

s=pd.DataFrame(student_data,columns=['iq','marks','package'])
print(s)

##Using dictionary

student_dict={
    'iq':[100,120,80,90],
    'marks':[80,90,50,80],
    'package':[10,12,6,8]
}

s1=pd.DataFrame(student_dict)
print(s1)

##Using read_csv
 
m=pd.read_csv('csv files\movies.csv')
movies=pd.DataFrame(m)
#print(movies)

i=pd.read_csv('csv files\ipl-matches.csv')
ipl=pd.DataFrame(i)
#print(ipl)

###DataFrame Attributes and Methods

##shape
#it is used to get the number of rows and columns in a dataframe

print(movies.shape)

##dtypes
#to know about the datatypes of dataframe

print(movies.dtypes)
#it gives u a series as there are multiple columns of data

##index
#to get the index of data 

print(movies.index)
#it gives a range of index with starting and ending value

##columns
#to get the all column name from dataframe

print(movies.columns)

##values
#to get all the values from data

print(student_dict.values())
#it gives value in numpy array

##head and tall

#head-> it provides data of top 5 rows to give preview about the data
print(movies.head())
#we can also customize it by providing values in it

#tail-> it provides data of last 5 rows to give preview about the data
print(movies.tail())
#we can also customize it by providing values in it

##sample
#it provide random value from data

print(movies.sample())
#we can also get more values from sample by providing value in it
print(ipl.sample(5))

##info
#it provides high level data like missing values,data type etc..
print(movies.info())

##describe
#it gives mathematical summary of data on numerical data

print(movies.describe())

##is_null
#to check the missing values in data

print(movies.isnull().sum())
#sum() is used to count all the missing values in a go otherwise isnull provides the boolean values in return

##duplicated
#to check whether a data is having any duplicate value or not

print(movies.duplicated().sum())

##rename
#it is used to rename the column name

#student_data.rename(columns={'marks':'percent','package':'mark'})
#this function is not working in vscode but syntax is same

###MATHS METHODS

##sum/max/min/mean/std/var/median
#if we apply sum on whole dataset then it will perform sum operation on whole data whether it is integer or not..

#print(ipl.sum()) not working in vscode but will work in google collab

#if we want to apply sum on rows
#print(movies.sum(axis=1))
print(s.sum())

#same things we can apply with different functions...


###SELECTING COLUMNS FROM DATAFRAME

##Using single cols
print(movies['title_x'])#in this way we can fetch a single column from a data

##Using multiple cols

print(movies[['title_x','year_of_release','actors']])


###SELECTIONG ROWS FROM DATAFRAME

##iloc
#it searches using index positions

#single row
print(movies.iloc[0])#it is fetching the single row using iloc

#multiple row
print(movies.iloc[0:5])#to fetch multiple movies at a time
#it works same as python slicing , we can do all the operation which can be performed using slicing

#fancy indexing
#if we want to fetch 0,4 and 5th movie
movies.iloc[[0,4,5]]


##loc
#searches using index labels

student_data={
    'name':['hitesh','isha','nitin','makhan'],
    'iq':[100,120,80,90],
    'marks':[80,90,50,80],
    'package':[10,12,6,8]
}

students=pd.DataFrame(student_data)
students.set_index('name',inplace=True)#to set the index column manually

#fetching one item 
print(students.loc['hitesh'])

#fetcing multiple item
print(students.loc['hitesh':'nitin'])#here last value is included 

#fancy indexing
print(students.loc[['hitesh','isha','makhan']])

#here also all the features of slicing we can use just there is change is that here last value is included 

##selecting both rows and columns at a time

#if we want the data of first three movies with first three columns
print(movies.iloc[0:3,0:3])

#same using loc
print(movies.loc[0:2,'title_x':'poster_path'])

