import random as r
x="i am happy"
print(r.sample(x,2))

#everytime it gives different output
import random as r
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)

import random as r
a=[1,2,3,4,5,6]
print(r.choice(a))
b="welcome back"
print(r.choice(b))

a=r.random()
print(a)

#will return random number between 0.0 to 1.0
#0.0 includes 1.0 excludes
import random as r
print(r.randint(20,30))
a=[10,20,30,40,50]
print(r.choices(a,k=10))
s="hello friday"
print(r.choices(s,k=3))
print(r.uniform(5,10))

note:in the above program u have to use only k for choices

#to find out all the functions in a module
import random as r
z=dir(r)
print(z)

#DISPLAY WHOLE YEAR CALENDAR
import calendar
print("full calendar")
print(calendar.calendar(2022))
print("particular month")
print(calendar.month(2023,1))
print("set first day of week")
calendar.setfirstweekday(calendar.MONDAY)
print(calendar.month(2023,5))

#prg-display date time
import datetime
a=datetime.datetime.now()
print(a)

sv=a.strftime("%y")
fv=a.strftime("%Y")
print("year short version",sv)
print("year long version",fv)

#functions
def sample():
    print("great day")
    print("happy time")
sample()
print("today")
sample()

#multiplying 3 numbers taking user input

#without arg without return value
def multi():
    a,b,c=int(input("enter a:")),int(input("enter b:")),int(input("enter c:"))
    prod=a*b*c
    print(prod)
multi()

#without arg with return value

def multi():
    a,b,c=int(input("enter a:")),int(input("enter b:")),int(input("enter c:"))
    prod=a*b*c
    return prod
    
res=multi()
print(res)

#with arg without return value
def multi(a,b,c):
    prod=a*b*c
    print(prod)
multi(1,2,3)

#user input
def multi(a,b,c):
    prod=a*b*c
    print(prod)
a,b,c=int(input("enter a:")),int(input("enter b:")),int(input("enter c:"))
multi1(a,b,c)

#with argument ,with return value
#static input
def multi(a,b,c):
    prod=a*b*c
    return prod
res=multi(1,2,3)
print(res)

#user input
'''def multi(a,b,c):
    prod=a*b*c
    return prod
a,b,c=int(input("enter a:")),int(input("enter b:")),int(input("enter c:"))
res1=multi(a,b,c)
print(res1)'''

#lemons program using functions type 1
def lemons:
    a,b,c=int(input("enter a:")),int(input("enter b:")),int(input("enter c:"))
    s=a+b+c
    print(s)    
    if s>21:    
    print("the num exceeds",s-21)
    elif s<21: 
    print("the num includes",21-s)
    elif:
    print("the num is 21")

#find factors of the given munber using fun type 2
n=int(input("number :"))
for i in range(1,n+1):
      if n%i==0:
           print(i)                 

#print mul tale of the given number using funcs type 3

def multi_table(n):
    for i in range(1,10):
         print(i,"X",n,"=",i*n)
n=int(input("which table :")
multi_table(n)      
    
    
# find out sum of digits of given number using func type 4
def digits(n):
    sum=0
    while n!=0:        
        rem=n%10        
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the number:"))
res=digits(n)
print(res)

#recursion
def display():
    n=int(input("enter a number"))
    if n==1:
        display()
    else:
            print("over")
display()



def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result=fact(5)
print(result)

#fibnoci series
n=int(input("enter number: "))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end =" ")
    count +=1
    a=b
    b=sum
    sum=a+b

#function returns more values:
# addition and subtraction of 2 numbers in one function

def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)

#variable length method
def summ(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
summ(10,8,1,2)




    


            












