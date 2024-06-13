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

print(pd.DataFrame(student_data,columns=['iq','marks','package']))

##Using dictionary

student_dict={
    'iq':[100,120,80,90],
    'marks':[80,90,50,80],
    'package':[10,12,6,8]
}

print(pd.DataFrame(student_dict))

##Using read_csv

