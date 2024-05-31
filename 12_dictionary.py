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

