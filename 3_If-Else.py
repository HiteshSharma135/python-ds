#Syntax of if-else statement

#if condition:
    #code
#else:
    #code

#login program and indentation
#email: hitesh@gmail.com
#password:1234

email=input('enter email')
password=input('enter password')

if email=='hitesh@gmail.com' and password=='1234':
    print('welcome')
elif email=='hitesh@gmail.com' and password!='1234':
    print("wrong password , input password again...")
    password=input('enter password')
    if password=='1234':
        print('entered finally')
    else:
        print('tumse na ho payega')
     
else:
    print('wrong info')


### Find minimum of three numbers

a=input('enter first num')
b=input('enter second num')
c=input('enter third num')

if a<b and a<c:
    print('smallest is ',a)
elif b<c:
    print('smallest is ',b)
else:
    print('smallest is',c)


###Menu driven program

fnum=int(input('enter first number'))
snum=int(input('enter second number'))
op=input('enter operator')

if op=='+':
    print(fnum + snum)
elif op=='-':
    print(fnum-snum)
elif op=='*':
    print(fnum*snum)
else :
    print(fnum/snum)

