'''d={n:n*n for n in range(1,5)}
print(d)'''

'''#CALCULATING PRODUCT PRICE FOR 5 UNITS
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in old.items()}
print(new)'''

'''#WITH CHECKS
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)'''

'''#create a list with  8 customer names display a dictionary which has customers names along with discounts for them from a particular shop
import random
c=["ali","honey","joy"]
c_dict={names:random.randint(1,100)for names in c}
print(c_dict)'''

'''#using zip function in 2 lists
l1=['a','b','c']
l2=[1,2,3]
d={a:b for (a,b) in zip(l1,l2)}
print(d)'''

'''#create 2 lists in one is student names nd their total in second list their percentage is needed with diff iterables using zip
import random
stu_names=list(map(str,input("enter names:")))
marks=[]
for i in range(len(stu_names)):
    a=(random.randint(300,500) /500)*100
    marks.append(a)
my_dict={x:y for(x,y) in zip(stu_names,marks)}
print(my_dict)'''

'''#get one string as input along with character find out nd display whether the character is present or not
s=input("enter a string:")
c=input("enter a char:")
if c in s:
    print("present")
else:
    print("not present")'''

'''#second method
st=input("enter the string:")
char=input("enter req char:")
a="yes" if char in st else no
print(a)'''

'''#third method
s=input("enter:")
char=input()
for i in s:
    if i==char:
        flag=1
        break
    else:
       flag=0
if flag==1:
    print("present")
else:
    print("not present")'''
             

'''#check whether the string is palindrome or not
x="madam"
w=" "
for i in x:
    w=i+x
if(x==w):
    print("yes")
else:
    print("no")'''

'''#after getting one string check whether the spaces are present or not and if present print the spaces
s=input("enter a string:")
count=0
for i in s:
    if i==" ":
        count+=1
print(count) '''

'''#create a list with vowels get one string as input,count vowel from the string nd display the result
l=["a","e","i","o","u"]
n=input("enter string")
count=0
for i in n:
      if i in l:          
         count+=1
print(count)'''

'''#math module
import math
print("ceil 12.5:",math.ceil(12.5))
print("floor 12.5:",math.floor(12.5))
print("sort 345:",math.sqrt(345))
print("power 2,3:",math.pow(2,3))
print("remainder 10,3:",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b)'''




        

    


    
    
