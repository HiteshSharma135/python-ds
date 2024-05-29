###Operators in python

#Arithmetic operators
print(2+5)
print(5-6)
print(5*5)
print(2/3)
print(5//2)#integer division if answer is in decimal it gives only integer value
print(5%2)#modulus -> it gives remainder
print(5**2)#power of operator

#Relational operators 

print(4<4)
print(4>4)
print(4<=4)
print(4>=4)
print(5!=4)
print(2==2)

#Logical operators

print(1 and 0)
print(1 or 0)
print(not 1)     

#Bitwise operators

#bitwise and
print(2 & 3)#it takes the binary values of 2 and 3 then perform binary operation 

#bitwise or
print(2 | 3)

#bitwise xor
print(2^3)

#bitwise not
print(~3)

#Assignment operator(=)
a=2
#it can be used with different operators also
a+=2
#a=a+2
print(a)

#Note :- a++ ++a not use in python 


#Membership operator
#these operator are used to check whether any particular info. present or not in given data
# in/not in (types)
#it return boolean values
print('D'not in'Delhi')

print(1 in [2,3,4,5,6])




#program to find the sum of number entered by user

number=int(input("enter the 3 digit number"))
# firstly we need all the 3 digits separately 
#to get the last digit just modulus it by 10

x=number%10
#last digit accessed

#now to get the second digit we need to smaller the number 
# use // operator to get the 2 digit integer value
number=number//10

y=number%10

number=number//10

z=number

print(x+y+z)




