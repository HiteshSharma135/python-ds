#A tuple is similar to a list.The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list ...

#In short, a tuple is an immutable list.A tuple cannot be changed once it is created 

#Characteristics of tuple:-
#Order matters 
#Unchangeble
#Allows duplicate



###CREATING TUPLES

##Empty tuple
t1=()
print(t1)

##Single item tuple

t1=(2)#this is  the wrong way of creating tuple 
print(t1)#it will the number 2 as output not in tuple format
print(type(t1))#to check the type of tuple it shows int
#this is not the correct way of creating single item tuple

t1=(2,)#this is the correct way of creating single item tuple
print(t1)
print(type(t1))

##Homogeneous tuple
t1=(1,2,3,4)
print(t1)

##Hetrogeneous tuple

t3=(1,2,3,(5,6),True,'hitesh')
print(t3)

##2D tuple

t4=(1,2,3,(5,6))
print(t4)

##Using type conversion

t5=tuple('hitesh')
print(t5)


###ACCESSING ITEMS FROM TUPLE

##Indexing
#it is similar which we read in lists
#positive indexing
t5=(1,2,3,4,5)
print(t5[1])

#negative indexing
print(t5[-1])

#if we want to access the index which is not in the tuple then it will show error

##Slicing   
#it also same as we read in list

print(t5[0:4])

print(t5[-4:-1])

print(t5[0:4:2])

print(t5[::-1])#to reverse the tuple

###EDIT ITEMS IN TUPLE 
t5=(1,2,3,4,5)
#t5[0]=100
print(t5)# it will show error as tuple are immutable just like strings

###ADDING ITEMS IN TUPLE
#not possible as tuples are immutable

###DELETING ITEMS IN TUPLE
#in tuple we can delete the whole tuple but cannot delete the specific items in tuple as it would mean to changes in the tuple (which is not allowed)
t5=(1,2,3,4,5)
del t5
#print(t5)#it will show error as tuple is  deleted

t5=(1,2,3,4,5)
#del t5[1]#this will not work as not allowed in tuple


###OPERATIONS ON TUPLE

##Arithmetic(+,*)

# +operation
t=(1,2,3)
t1=(4,5,6)
print(t+t1)#it will concatenate/merge both the tuple

# *operation

print(t*3)#it will print the tuple 3times in a row

##Membership(in/not in)
t1=(4,5,6)

print(1 in t1)#it will check whether 1 is in tuple or not then provide boolean answer

print(1 not in t1)

##loops
t1=(4,5,6)
for i in t1:
    print(i)

#it is same as list


###TUPLE FUNCTIONS

##len/sum/min/max/sorted

t1=(4,5,6)
print(len(t1))# to check the length of tuple

print(sum(t1))#to access the sum of tuple items(all the items must be in integer)

print(max(t1))#to find maximum item in tuple

print(min(t1))#to find minimum item in tuple

print(sorted(t1))#to sort the tuple in ascending order
print(sorted(t1,reverse=True))#to sort the tuple in descending order

##Count
#it is used to count the occurence of specific item in a tuple

t1=(4,5,6)
print(t1.count(5))

##Index
#it is used to get the index of tuple item 
t1=(4,5,6)
print(t1.index(5))

#if we want to get the index of item which is not in tuple list then it will show error

###DIFFERENCE BETWEEN TUPLE AND LIST
#syntax
#mutability(tuples are immutable)
#speed(tuples are faster)
#memory(tuple take less memory)
#built in functionality(list have more functionality)
#error prone(tuple is more error free
#usability


###Special syntax

##tuple unpacking
a,b,c=(1,2,3)
print(a,b,c)


#to swap the values
a=1
b=2
a,b=b,a
print(a,b)

#if we want to only two relevant values from tuple

a,b,*others=(1,2,3,4,5)
print(a,b)
print(others)

###Zip function in tuples

a=(1,2,3,4)
b=(5,6,7,8)
zip(a,b)#it will a and b and create a zip object

tuple(zip(a,b))#it will give tuple of tuple

