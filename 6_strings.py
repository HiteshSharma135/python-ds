# In python specially ,strings are a sequence of UNICODE characters

##Creating Strings

s='hello'
s="hello"
s='''hello'''#it is used to multiline strings
s="""hello"""
s=str('hello')
print(s)



##Accessing Substrings from string

#Indexing
s='hello world'
#whenever we create a string python automatically assign the indexing to the string starting from 0 to n-1, it is positive indexing
print(s[0])
#to access first character

#Negative indixing
s='hello world'
#in this negaive indexing , indexing is done from right to left staring from -1 to so on ,,, it is used when we don't know the length of string and want to access the last character
print(s[-1]) 


#Slicing (it is used when we need to access more than one character from string)
s="hello world"
print(s[0:5])
#in case of slicing we provide range from where we want to start till end , in addition to that last index is not included 
print(s[2:])
#here we skip the second range in that case it will go till end 
print(s[:5])
#same with the starting range
print(s[:])
#it will print the whole string
print(s[0:6:2])
#here the third variable is for step size (that is it will skip the 2 characters in a string , then print it )
print(s[6:0:-1])
#it will print the string in reverse (for -ve stepsize the staring range must be greater than the ending range)

print(s[::-1])
#to reverse the entire string 



##Editing and Deleting the String 

#Editing

s="hello world"
#s[0]='H'
#It will show error 
#In python strings are Immutable(if created once, cannot be edited)


#Deleting

s="hello world"
del s
#print(s)
#now while printing string s , it will show error as string is deleted now so cannot be printed

## Operations on Strings

#Arithmetic operations
#only + and * operator works on string
print('delhi'+' '+'mumbai')

print('delhi'*5)


#Relational Operator (every relational operator works on strings)

print('delhi'>'mumbai')#it will just compare the strings and give the answer in boolen values
