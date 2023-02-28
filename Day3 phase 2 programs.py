#creating a linked list we will do here multiple concepts in this program
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        if not temp:
            print('List is empty.')
            return
        else:
            print('Start:', end=' ')
            while temp:
                print(temp.data, end=' -> ')
                temp=temp.next
                #print('end')
    def insert(self,data):
         new_Node=Node(data)
     #if the linked list is empty
         if self.head is None:
             self.head = new_Node
        # if the data is smaller than the head
         elif self.head.data >=new_Node.data:
             new_Node.next=self.head
             self.head=new_Node
         else:
        #locate the node before insertion
             current=self.head
             while current.next and new_Node.data > current.next.data:
                current=current.next
        # insertion
             new_Node.next=current.next
             current.next=new_Node
    def delete(self,key ):
         #if the list is empty
         if self.head is None:
             print('deletion error: the list is empty')
             return
            # if the key is in head
         if self.head.data==key:
             self.head=self.head.next
             return
            # find position of first occurence of the element
         current=self.head
         while current:
             if current.data==key:
                 break
             previous=current
             current=current.next
             #if the key was not found
         if current is None:
             print('deletion error: key not found.')
         else:
             previous.next=current.next
 # __name is python special variable
if __name__=='__main__':
     #create an object
     LL= LinkedList()
     print('')
     #insert some nodes
     LL.insert(10)
     LL.insert(12)
     LL.insert(8)
     LL.insert(11)
     LL.insert(10)

     LL.printList()
     LL.delete(12)
     LL.delete(8)
     LL.delete(10)
     LL.printList()'''
     
'''import fn
fn.printing()

print(__name__)



print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=="__main__":
    f1()
    f2()
    f3()
print("name:",__name__) '''   

#double linked list
#create node
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()
        
                 
#insertion in dll
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start()
l.display()

#insertion at ending
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:   
    def __init__(self):        
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()

#inserting at position
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:   
    def __init__(self):        
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()



class dll:
    def __init__(self):
        self.head=None
         def insert_pos(self):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_pos()
l.display()

#dll delete start
class singlelinkedlist:
    def __init__(self):
        
        self.head=None
        
  
    def delete_beginning(self):        
        temp=self.head
        self.head=temp.next
        temp.next=None

#dll delete end        
    def delete_beginning(self):        
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
# dll delete position
   def delete_pos(self,pos):        
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
#circular linked list
#Represents the node of list.    
class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    
     
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
  #This function will add the new node at the end of the list.    
  def add(self,data):    
    newNode = Node(data);    
    #Checks if the list is empty.    
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
      #tail will point to new node.    
      self.tail.next = newNode;    
      #New node will become new tail.    
      self.tail = newNode;    
      #Since, it is circular linked list tail will point to head.    
      self.tail.next = self.head;    
     
  #Displays all the nodes in the list    
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty");    
      return;    
    else:    
        print("Nodes of the circular linked list: ");    
        #Prints each node by incrementing pointer.    
        print(current.data),    
        while(current.next != self.head):    
            current = current.next;    
            print(current.data),    
     
     
class CircularLinkedList:    
  cl = CreateList();    
  #Adds data to the list    
  cl.add("s");    
  cl.add("m");    
  cl.add("i");    
  cl.add("l"); 
  cl.add("e");  
  #Displays all the nodes present in the list    
  cl.display();            
        
        
        
            



        
       
  
            
        
        
