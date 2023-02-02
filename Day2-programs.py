#GUESSING A NUMBER

import random
n=random.randrange(1,50)
guess=int(input("enter any number: "))
while n!=guess:
    if guess < n:
        print("too low")
        guess=int(input("enter number again: "))               
    elif guess > n:
        print("too high!")
        guess=int(input("enter number again: "))
    else:
     break
print("you guessed is right!!")                   

#CONDITIONAL LOOPS
 FOR LOOP
 
for i in range(1,11):
    print(i)

    
for i in range(1,20):
    if(i%2==0):
        print(i)

        
for i in range(1,20):
    if(i%2!=0):
        print(i)

        
for j in range(2,11,2):
    print(j)
    
WHILE LOOP

i=1
while i<=10:
    print(i)
    i=i+1
    
i=2
while i<=20:
    if i%2==0:
       print(i)
    i=i+1
    
i=2
while i<=20:
    if i%2!=0:
       print(i)
    i=i+1
    
#INT OR FLOAT
n=10.3
res=n-int(n)
if res>0 or res!=0:
    print("float")
else:
    print("integer")

#WHICH ONE IS GREATEST
 n1,n2,n3=(int(input("enter n1:")),int(input("enter n2:")),int(input("enter n3:")))
if n1>n2 and n3:
    print(n1," is greatest")
elif n2>n1 and n3:
    print(n2," is greatest")
else:
    print(n3," is greatest")
    
#GIVEN NUMBER IS 500 OR NOT
n=int(input("enter number:"))
if n==500:
    print("given number is 500")
else:
    print("given number is not 500")


    
    
      
    
       
    
    


