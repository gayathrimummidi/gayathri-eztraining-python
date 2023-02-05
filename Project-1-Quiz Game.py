q1='''Which animal is known as the ‘Ship of the Desert?
a.elephant
b.tiger
c.camel
d.lion'''
q2='''How many sides are there in a triangle?
a.1
b.2
c.3
4.5'''
q3='''Who was the first man to walk on the moon?
a.Neil Armstrong
b.Edwin
c.Charles
d.Alan Bean'''
q4='''Which day is observed as World Environment Day?
a.March 10
b.June 5
c.January 20
d.August 15'''
q5='''How many players are there in a cricket team?
a.5
b.6
c.10
d.11'''
questions={q1:"c",q1:"c",q3:"a",q4:"b",q5:"d"}
name=input("Hi whats ur name")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this questions (yes/no)")
    if flag1=="yes":
         continue
    ans=input("enter your answer")
    if ans== questions[i]:
        print("Wow!you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("your current score is",score)
    flag2=input("Do you want to quit? type (yes/no)")
    if flag2=="yes":
        break
print("your total score is",score)


    
