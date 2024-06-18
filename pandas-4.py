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
        'cgpa':['eee','it','cse',np.nan,np.nan,'me','ce',np.nan],
        'package':[4,5,6,np.nan,np.nan,8,9,10]
    }
)

#one column
#movies.sort_values('title_x') #this is in ascending order
#movies.sort_values('title_x',ascending=False)#this is in descending order

#if we perform sort_values on a column where there are Nan values then by default all the NaN values will be in the last
#students.sort_values('name')

#if we want all the NaN values on top 
#students.sort_values('name',na_position='first')

#multiple column
#movies.sort_values(['year_of_release','title_x'])#both are in ascending order
#movies.sort_values(['year_of_release','title_x'],ascending=[True,False])#year in ascending and title is in descending


##rank(series)
batsman=pd.read_csv('csv files/batsman_runs_ipl.csv')
print(batsman.sample())

batsman['batsman_run'].rank(ascending=False)
#giving rank on the basis of runs
batsman['batting_rank']=batsman['batsman_run'].rank(ascending=False)
#creating a new column having rank of each batsman

print(batsman.sort_values('batting_rank'))

##sort_index(series and dataframe)
#it sorts the data based on index
marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
marks_series=pd.Series(marks)

marks_series.sort_index(ascending=False)

#print(movies.sort_index())

##set_index(dataframe) --> inplace
print(batsman.head())
#if we dont want the bydefault index and want a customize index in that case we can use set_index....
batsman.set_index('batter')
print(batsman.head())

##reset_index(series and dataframe) -->drop parameter
#if we want to reset the index to previous ... we use reset index
#it is also not a permanent operation 
batsman.reset_index()

#if we want to replace  the existing index without loosing 
batsman.reset_index().set_index('batting_rank')

#if we apply reset_index on series it would become dataframe
print(type(marks_series.reset_index()))

##rename(dataframe) -->index

#movies.rename(columns={'imdb_id':'imdb','poster_path':'link'})
#working in google collab

#with the help of rename we can change the index name also
#movies.rename(index={'Uri: The Surgical Strike':'Uri'})

##unique(series)
#it counts all the unique values including nan values
temp=pd.Series([1,1,1,2,2,3,4,5,3,4,5,np.nan,np.nan,np.nan])
print(temp.unique())

##nunique(series + dataframe)
#it is used to count the unique values...
#it does not count nan values

len(temp.unique())#it will count  the nan values
temp.nunique()#it won't count the nan values

###METHODS FOR NAN VALUES

##isnull(series + dataframe)
#it gives output in boolean form as in true-> missing value present,, false-> missing value not present
students['name'].isnull()

##notnull(series + dataframe)
#it is opposite of isnull as true-> missing value not present,, false-> missing value present
students['name'][students['name'].notnull()]

##hasnans(series )
#it tells about the whole column either any missing value is present in the column or not...
#it gives if there is missing value
#students['name'].hasnans()

##dropna(series + dataframe) -->how parameter -->work like or
#it is used to remove the nan values
students['name'].dropna()
#it will drop the missing values from the series

students.dropna()
#it will drop the missing values from the dataframe.. as in if there is any missing values in a row ,, it will the remove the whole row
#it is the default behaviour of dropna

#to overwrite the default behaviour of dropna() as if we want to remove only those rows which is having missing values in all the columns 
students.dropna(how='all')

#we can also customize the logic of dropna() as in if we want to remove only those rows which is having missing values in its name column
students.dropna(subset=['name'])


##fillna(series + dataframe)
#it is used to fill the values in missing values

students['name'].fillna('unknown')
#now where there was missing value now it is replaced by unknown

#we can also apply custom logic in place of missing values as if there is any missing value in package column it will be filled by the mean of all the packages
students['package'].fillna(students['package'].mean())

#another way is that we can fill the missing values with the before element with.. as in if there is nan element and before that it is 45 then in place of nan 45 will be placed... it is called forward fill
#students['name'].fillna(method='ffill')
#another is bfill --> before fill

##drop_duplicates(series + dataframe)
#it helps in dropping the duplicate rows
students.drop_duplicates()
#it will remove all the rows which are duplicate

##find the last match played by virat kohli in delhi
ipl['all_players']=ipl['Team1']+ipl['Team2']

def did_kohli_play(player_list):
    return 'V Kohli' in player_list

ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)
ipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play']==True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first')


##drop(series + dataframe)
temp=pd.Series([10,2,5,7,8,96,54])
#if we want to drop the row having 0 and 6 index
temp.drop(index=[0,6])
#if we want to drop the branch and cgpa column  
#  students.drop(columns=['branch','cgpa'])
#if we want to drop the rows having 0 and 5 index 
students.drop(index=[0,5])

##apply(series + dataframe)
points_df=pd.DataFrame(
    {
        '1st point':[(5,2),(-8,7),(-4,-5),(2,1),(0,0)],
        '2nd point':[(1,2),(4,-5),(-6,-8),(0,0),(-2,-3)]
    }
)

#if we want to calculate the euclidian distance of 1st point and 2nd point and then store it in new column

def euclidian(row):
    pt_a=row['1st point']
    pt_b=row['2nd point']

    return ((pt_a[0]-pt_b[0])**2 + (pt_a[1]-pt_b[1])**2)*0.5

points_df['distance']=points_df.apply(euclidian,axis=1)
print(points_df)