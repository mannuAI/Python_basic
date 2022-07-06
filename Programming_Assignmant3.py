#!/usr/bin/env python
# coding: utf-8

# # Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


num=float(input("Enter the numbers: "))
if num>0:
    print("positive number")
elif num==0:
    print("this is zero")
else:
        print ("this is negative number")


# # Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


num=float(input("Enter the numbers: "))
if (num % 2) ==0:
    print ("This is even number")
else:
    print ("This is odd number")


# # Write a Python Program to Check Leap Year?

# In[6]:


year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
else:
    print("not a leap year".formate.year())


# # Write a Python Program to Check Prime Number?

# In[13]:


num=int(input("Enter the numbers: "))
flag=False
if num>1:
    for i in range (2, num):
        if (num % i)==0:
            flag=True
            break
            if flag:
                print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# # Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[16]:


lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




