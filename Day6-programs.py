'''a=100
b=0
print(a/b)'''

#exception handling
'''a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("num cannot divided by zero",e)
finally:
    print("end")'''


'''a=10
try:
    b=int(input("enter the input"))
    print(a/b)
except ZeroDivisionError as e:
    print("cannot be divisible",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("resource closed")'''

#raise is used to interupt the program flow and raise an exception

'''x=10
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is even number...correct")'''

#OOPS
'''class computer:
    def config(self):
        print("yes")
lenova=computer()
lenova.config()
dell=computer()
dell.config()'''

#constructor
'''class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID:%d \nName: %s" %(self.id,self.name))
emp1=Employee("John",101)
emp2=Employee("David",102)
emp1.display()
emp2.display()'''

#variable accessing in class and method
'''class computer:
    a=10
    b=20
    print("class variable inside class",a)
    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)
lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()'''





      
              


              
    
    

    
          


