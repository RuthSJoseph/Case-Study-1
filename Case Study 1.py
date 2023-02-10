#!/usr/bin/env python
# coding: utf-8

# In[10]:


#QUESTION 1 

marks=int(input("Enter Marks : "))
if marks<25:
  print("F")
elif marks>=25 and marks<45:
  print("E")
elif marks>=45 and marks<50:
  print("D")
elif marks>=50 and marks<60:
  print("C")
elif marks>=60 and marks<80:
  print("B")
else:
  print("A")


# In[11]:


#QUESTION 3

length=int(input("Enter Length : "))
breadth=int(input("Enter Breadth : "))
if length == breadth:
  print ("Yes, it is square")
else:
  print ("No, it is only Rectangle")


# In[18]:


#QUESTION 4


held=int(input("Number of classes held : "))
att=int(input("Number of classes attended : "))
percent=float(att/held)*100
print ("Attendence is",percent)
if percent>= 75:
  print ("You are allowed to sit in exam")
else:
  print ("Sorry, you are not allowed. Attend more classes from next time.")


# In[39]:


#QUESTION 5


list1= []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
  
    list1.append(ele) 
      
print(list1)
total = 0
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum : ", total)

def evenodd(list1): 
   Even_list=[]
   Odd_list=[] 
   for i in list1: 
      if (i % 2 == 0): 
         Even_list.append(i) 
      else: 
         Odd_list.append(i) 
   print("Even lists:", Even_list) 
   print("Odd lists:", Odd_list) 
    
evenodd(list1)


# In[31]:


#QUESTION 7

import math 
  

def equationroots( a, b, c): 
  
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 

    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a == 0: 
        print("Input correct quadratic equation") 
  
else:
    equationroots(a, b, c)


# In[36]:


#QUESTION 8

num = list(range(11))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum)) 
    previousNum=i


# In[25]:


#QUESTION 9

start = int(input("Enter the lower bound: "))
stop = int(input("Enter the upper bound: "))
print("Prime numbers between", start, "and", stop, "are:")
for val in range(start, stop):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")


# In[37]:


#QUESTION 10

num = int(input("Enter the Range Number: "))
First_val = 0
Second_val = 1
for n in range(0, num):
           if(n <= 1):
                      next = n
           else:
                      next = First_val + Second_val
                      First_val = Second_val
                      Second_val = next
           print(next)

