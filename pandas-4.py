import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

df=pd.read_csv('csv files/ipl-matches.csv')
ipl=pd.DataFrame(df)

df1=pd.read_csv('csv files/movies.csv')
movies=pd.DataFrame(df1)

###filtering a dataframe
print(ipl.head(2))

##find all the final winners in all ipl seasons

mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]
print(new_df[['Season','WinningTeam']]) 

##how many super overs finishes have occured in all the ipl matches

ipl[ipl['SuperOver']=='Y']#it will the detail of all the matches of super over
#to get the count we use shape which count the number of rows 
print(ipl[ipl['SuperOver']=='Y'].shape[0])

##how many matches csk won in kolkata

c=ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam']=='Chennai Super Kings')].shape[0]

print(c)

##toss winner is match winner in percentage

print((ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)

##movies with rating higher than 8 and votes >10000

print(movies.head(2))

print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000 )].shape[0])


##action movies with rating greater than 7.5

mask1= movies['genres'].str.split('|').apply(lambda x:'Action' in x)
#here we use str first then split because we cannot use split without str and ,,,, apply function is used to apply custom logic (on the genre where there is action )
#second method (in this way also we can get the same result)
#mask1= movies['genres'].str.contains('Action')

mask2= movies['imdb_rating'] > 7.5

print(movies[mask1 & mask2])

###ADDING NEW COLS

##completely new cols
movies['Country']='India'
print(movies.head(2))

##from existing cols
#suppose we want to create a column name called lead actor where actor would be fetch from the actors column where (first actor will be treated as lead actor)

movies.dropna(inplace=True)
movies=movies['lead_actor']=movies['actors'].str.split('|').apply(lambda x:x[0])
#this will not work because there are missing values in the data because pandas treat missing values as float ... to overcome that we have to drop the nan values from the data set...

print(movies.head(2))

###IMPORTANT DATAFRAME FUNCTIONS

##astype
#it changes the datatype of any given column

ipl['ID']=ipl['ID'].astype('int32')


#Use category dtype when you have a column with a limited number of unique values (categories) and you want to save memory and improve performance for operations involving that column. It's especially useful for columns that are naturally categorical, like gender, country names, or any nominal/ordinal data.


##value_counts(series and dataframe)
#it will count the numbers which are repeated in a row

marks=pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

print(marks)

marks.value_counts()

#find which player has won most mom award in finals and qualifiers
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

#toss decision plot

print(ipl['TossDecision'].value_counts().plot(kind='pie'))
#plt.show(block=True)

#matches played by each team

print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending= False)) 


##sort_values(series and dataframe)
students=pd.DataFrame(
    {
        'name':['hitesh','isha','mayank',np.nan,'nitin',np.nan,'makhan',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan],
        'cgpa':['eee','it','cse',np.nan,np.nan,'me','ce',np.nan]
        'package':[4,5,6,np.nan,np.nan,8,9]
    }
)

#one column
movies.sort_values('title_x')#this is in ascending order
movies.sort_values('title_x',ascending=False)#this is in descending order

#if we perform sort_values on a column where there are Nan values then by default all the NaN values will be in the last
students.sort_values('name')

#if we want all the NaN values on top 
students.sort_values('name','na_position='first'')

#multiple column
movies.sort_values(['year_of_release','title_x'])#both are in ascending order
movies.sort_values(['year_of_release','title_x'],ascending=[True,False])#year in ascending and title is in descending


##rank(series)
