#happy number
def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
           r=n%10
           s=s+r**2
           n=n//10            
        return s               
n=int(input("enter the num:"))
res=n
while(res!=1 and res!=4):
     res=happy(res)
if res==1:
     print("happy number")
else:
     print("not a happy number")                  

#protected
class encap:
    __a=10
    c=20
    def encapfunction(self):
        __b=200
        print("encap function-accessing protected")
        print(self.__a+10)

obj=encap()
print(obj.__a)
obj.encapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(___a)
    def encapfunction(self):
        print("encap function")
        print(self.___a)
obj=encap()
obj.encapfunction()
print(obj.___a)

#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with all arguments")
obj.display(20,30)
print("with one argument")
obj.display(10)

#polymorphism
class vijayawada():
    def placename(self):
        print("vijayawada placement is KLU")
    def student(self):
        print("Yes - vijayawada")
    def which_year(self):
        print("3rd year")
class hyd():
    def placename(self):
        print("hyd placement is HYD-KLU")
    def student(self):
        print("Yes - HYD")
    def which_year(self):
        print("3rd year-hyd")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()

#creating node-declaration and creation
class Node:
    def ___init___(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def ___init___(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()

#example program of linked list
class Node:
    def ___init___(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def ___init___(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()

#inserting at end
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def _init_(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp  = first node
            while temp:
                print(temp.data,"->",end=" ")
                #tempdata means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
#node creation - initialization
n=Node(10)  #so n.data in node class will be 10
obj.head=n  #assigning first node as head
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.insert_end(1111)
obj.display()  

#inserting at beginning
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def _init_(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("befire inserting 100")
obj.display()
print(" ")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print(" ")
print("after inserting 555")
obj.insert_beginning(555)
obj.display() 


#inserting at given position
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def _init_(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            #np.data=data         not required
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp  = first node
            while temp:
                print(temp.data,"->",end=" ")
                #tempdata means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
n=Node(10)  
obj.head=n  
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.insert_position(3,100)
obj.display() 



#single linkedlist user input
class Node:
    def _init_(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def _init_(self):
        self.head = None
        self.last_node = None
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
n = int(input('how many elements would you like to enter'))
for i in range(n):
    data = int(input('enter data item'))
    a_llist.append(data)
print('the linked list:',end = ' ')
a_llist.display()



        
                   

              
    
