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
#with the help of format function we can insert the value of variable in a given string

name='hitesh'
gender='male'
print('my name is {} and my gender is {}'.format(name,gender))
#in this order matters of variable

print('my name is {1} and my gender is {0}'.format(gender,name))
#we can decide the positioning in it by providing the order number in it 



#####NOTE :- there may be doubt that as we know that string is immutable so how can we run these function on strings as it change the initial string so answer is that ... it doesnot changes the original string it makes the copy of original string and make changes in it and the original string remains same.. see example

s='india'
print(s.capitalize())
print(s)
#with the above example we can see that there is no change in the original string

#isalnum 
#this function is used to check whether the given string contains the alpha numerics or not
#it provides output in boolean format
s='hitesh1234'
print(s.isalnum())


#isalpha
#this function is used to check whether the given string contains the alphabets or not
#it provides output in boolean format

a='hitsh11'
print(a.isalpha())

#isdigit
#this function is used to check whether the given string contains the digits or not
#it provides output in boolean format

num='1234'
print(num.isdigit())

#isidentifier
#this function is used to check whether the given string is following the rules of identifier or not
#it provides output in boolean format

i='name1'
print(i.isidentifier())


###some important functions

#split
#this function just break the strings word by word and added to the python list

str='hey my name is hitesh'
print(str.split())

#we can also split the string into particular word .. for ex
print(str.split('is'))
#break the sentence on the bais of "is " word 


#Join 
#it is opposite of split function as it joins the words to make a string

print(" ".join(['hey', 'my', 'name', 'is', 'hitesh']))
#here joining of string is based on the space
print("-".join(['hey', 'my', 'name', 'is', 'hitesh']))
#here joining of string is based on the - character


#Replace
#this function is used to replace a particular word with the other word
#it just find that particular word that is to be replace and replace that word
rep='hy name is india'
print(rep.replace('india','hitesh'))


#Strip 
#this function is used to remove the spaces from the string from starting and ending of string
#it can also be used to remove the unwanted characters from the string this also in same manner starting or ending characters

name='hitsh sharma    '
print(name.strip())

name1=",,,,,,,,,,,ggggggggggggg sharma"
new=name1.strip(" ,g")
print(new)




