###common functions (these are the functions which work on every datatype)


#len
#it calculates the length of characters including the space
print(len('hello world'))

#max
#it extract the maximum character from string on the basis of its ASCII values
print(max('hello world'))

#min
#it extract the minimum character from string on the basis of its ASCII values
print(min('hello world'))

#sorted
#it sorted the string in the ascending order on the basis of its ASCII values and it gives output in list(datastructure)
print(sorted('hello world'))

#to print in descending order 
print(sorted('hello world',reverse=True))



###function (which work only on strings)

#Capitalize
#it just capitalize the first word of string

s='hello world'
print(s.capitalize())

#Title
#it capitalize the first letter of every word in a string
print(s.title())

#Upper
#it just convert the whole string in upper case
print(s.upper())

#Lower
#it just convert the whole string in lower case
print(s.lower())

#Swapcase
#it convert the lowercase letter to uppercase and vice versa
print(s.swapcase())


###More count related functions on string

#Count
#it will count the number of times a word occurs in a given string
s='hey i am hitesh sharma'
print(s.count('i'))

#find
#it is used to find at which index a word occurs in a string
print(s.find('am'))

#Index
#it is same function as find only difference is that if we put a word which is not in string it show error while in find function it shows -1 as output

#endswith
#to check whether string is ending with the particular word or not
#it gives output in boolean values
print(s.endswith('ma'))


#starts with
#to check whether string is starting with the particular word or not
#it also gives output in boolean values
print(s.startswith('i'))


#Format
#
