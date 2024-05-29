###loops in python
##while loop

#program to print the table

number=int(input("enter the number"))
i=1
while i<11:
    print(number,'*',i,'=',number*i)
    i+=1

#while loop with else

i=1

while i<3:
    print(i)
    i+=1

else:
    print('limit crossed')


#guessing game

import random

jackpot=random.randint(1,100)

guess=int(input("guess the number"))
counter=1

while guess!=jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")
    
    guess=int(input("guess the number"))
    counter+=1

else:
    print("correct guess")
    print("it takes you attempts",counter)



##for loop

#for loop can iterate on any data type i.e.(tuples,set,dictionary,string)
#in range first number is include and last is excluded
for i in range(1,11):
    print(i)


for i in range(1,11,2): #here 2 represent the iteration that is i+=2 (step size)
    print(i)

for i in range(10,0,-1):
    print(i)

for i in 'Delhi':
    print(i)



#program:- the current population of town is 10000. it is increasing at a rate of 10% per year.You have to write a program to find out the  population at the end of 10th year

curr_pop=10000

for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop=curr_pop/1.1


#Program to calculate 1/1!+2/2!+3/3!+.....

n=int(input('enter the value of n'))
fact=1
result=0

for i in range(1,n+1):
    fact=fact*i
    result=result+i/fact

print(result) 


###Nested loop

#to print the unique value pairs

for i in range(1,5):
    for j in range(1,5):
        print(i,j)


#pattern 
#*
#**
#***

rows=int(input("enter the number of rows"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end='')

    print()



#Pattern
1
121
12321
1234321

rows=int(input("enter the number of rows"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
        
    for k in range(i-1,0,-1):
        print(k,end='')

    print()

###Loop control statement

#Break statement

#example :- linear searching is an example of break when we are seaching for a data in large database when we find that data we apply break

for i in range(1,11):
    if i==5:
        break
    print(i)


#to print prime number in a given range 

lower=int(input("enter the lower range"))
upper=int(input("enter upper range"))

for i in range(lower,upper+1):
   for j in range(2,i):
       if i%j == 0:
           break
    
   else:
       print(i) 




#Continue Statement

for i in range(1,11):
    if i==5:
        continue
    print(i)

#example :- in e commerce if any product has stock then we skip it and move to next product


#Pass statement (it is used to pass the current condition or iteration to overcome the error , it is used in a scenario when we want to code under some condition but not right now so compiler just skip that iteration )

for i in range(1,10):
    pass








