#Dictionary in python is a collection of key values,used to store data values like map,which ,unlike other data types which hold only a single value as a element.
#In some languages it is known as map or associative arrays.
#dict={'name':'hitesh','gender':'male'}
#Characteristics:-
#mutable
#indexing has no meaning
#keys can't be duplicated
#keys can't be mutable items


###CREATE A DICTIONARY

##empty dictionary
d={}
print(d)

##1d dictionary 
dict={'name':'hitesh','gender':'male'}
print(dict)

##Dictionary with mixed keys
d2={(1,2,3):1,'hello':'world'}
print(d2)

##2D dictionary
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}
print(student)

##using sequence and dict function 
#d4=dict(1=1,2=2,3=3)
#print(d4)


##Duplicate keys
d5={'name':'sharma','name':'hitesh'}
print(d5)

##Mutable items as key
#d6={'name':'hitsh',[1,2,3]:2}#it will show error as there is list inside a dictionary which mutable 
#print(d6)
d6={'name':'hitsh',(1,2,3):2}#now it will work as tuple is not mutable
print(d6)


###ACCESSING ITEMS FROM DICTIONARY
new={'name':'hitesh','age':21}

#to access the items indexing is not allowed
#print(new[0])  it will show error

##to access the item we can pass the object name
print(new['name'])#it will provide the corresponding value to name

##get
#it same as above function
print(new.get('age'))

##accessing 2d dictionary 
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}
print(student['subject']['dsa'])#to access the marks of dsa

###ADDING KEY VALUE PAIR
##to add new key value pair in dictionary

new={'name':'hitesh','age':21}
new['gender']='male'
print(new)


##adding key values in 2d dictionary
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}

student['subject']['datascience']=78
print(student)

###REMOVING KEY VALUE PAIR


##pop
new={'name':'hitesh','age':21}
new.pop('name')#it will delete the corresponding key value pair
print(new)

##popitem
new={'name':'hitesh','age':21,'gender':'male'}
new.popitem()#it will delete the last key value pair
print(new)

##del
#it is used to delete whole key value pair or can be used as pop function
new={'name':'hitesh','age':21,'gender':'male'}
del new['age']
print(new)
del new
#print(new) it will show error as new is deleted

##clear
#it will delete all the key value pairs and make the dictionary empty
new={'name':'hitesh','age':21,'gender':'male'}
new.clear()
print(new)

###EDITING KEY VALUE PAIR

student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}

#if we want to update hte marks of dsa
student['subject']['dsa']=80
print(student)

###DICTIONARY OPERATIONS

##Membership
#in dictionary if we put in operations then it will search only in the keys not in values

s={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}

print('hitesh' in s)#it will give false as it will search in keys
print('name' in s)#now it will give true as name is the key

##Loops
#same as membership ,,  loops also works on the keys not on the values
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':'english'
}

for i in student:
    print(i) # now it will print all the keys
    #print(i,d[i])#to print key and values both(it is not working in vscode but will work in google collab)


###DICTIONARY FUNCTIONS

##len/sorted
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}
print(len(student))#it will print the length(number) of keys

print(sorted(student))#it will sort the keys in ascending order and give output in list

print(sorted(student,reverse=True))#to sort in descending order

##items/keys/values
student={
    'name':'hitesh',
    'college':'hbs',
    'sem':4,
    'subject':{
        'dsa':50,
        'oops':87,
    }
}

print(student.items())#it will show all the key value pairs in the form of tuple

print(student.keys())#to print all the keys

print(student.values())#to print all the values

##update

d1={1:2,2:4,3:6}
d2={2:5,3:8}

print(d1.update(d2))#it will update the values of d1 which is present in d2(will work in google collab)


###DICTIONARY COMPREHENSION

##program to print 1st 10 numbers and their squares

{i:i**2 for i in range(1,11)}

##using existing dict

distance={'delhi':1000,'mumbai':2000,'banglore':3000}

{key:value*0.62 for (key,value) in distance.items()}#to convert km to miles

##using zip
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
temp_c=[30.5,31.2,33,34.0,35.6,33.2,36.6]

print({i:j for (i,j) in zip(days,temp_c)})


##using if condition 
products={'laptop':10,'phone':15,'tablet':0}
#to show the products only whose stock is not zero

print({key:value for(key,value) in products.items() if value>0})
 

###NESTED COMPREHENSION

##print tables from 2 to 4

print({i:{j:i*j for j in range(1,11)}for i in range(2,5)})