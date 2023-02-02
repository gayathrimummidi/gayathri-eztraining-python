
#LIST TO LIST APPEND

numbers=[elements for elements in "great afternoon"]
print(numbers)



#creating list using existing list
l=["hyd","vzg","chennai","vjy"]
city=[]
for n in l:
    if "v" in n:
        city.append(n)
print(city)


l1=[2**x for x in range(2,10)]
print(l1)

l2=[a for a in range(100,201,20)]
print(l2)

l3=[1,2,3,4,5,6]
l4=[i for i in l3 if(i<5)]
print(l4)

#PROD AND SUM OF LIST
l=list(map(int,input("enter").split()))
print(l)
x=1
y=0
for i in l:
    x=x*i
    y=y+i
if x<=750:
    print("prod",x)
else:
    print("sum",y)


#PRINTING EVEN NO
    size=int(input("size"))
l=[]
for i in range(size):
    ele=int(input("size"))
    l.append(ele)
print(l)
for j in l:
    if(j%2==0):
        print(j)


#SUM AND AVERAGE
        l=[3,6,9,2,9]
count=0
for i in l:
    count+=i
avg=count/5
print(count)
print(avg)


#LIST OPERATIONS
l=[1,4,1,1,6,4,1,2]
len(l)
l.count(1)
l.append(400)
l.extend([100,200,300])
l.remove(1)
l.pop(-2)
l.reverse()
l.sort()'''


l=[1,2,3,2]
for i in range(len(l)):
    print(l[i])
    

l=[1,3,5,9.3,9.0,"dog","cat","laugh",23.2,12.0]
for i in range(len(l)):
    print(l[i])
    

