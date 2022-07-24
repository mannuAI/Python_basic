#!/usr/bin/env python
# coding: utf-8

# # Write a Python Program to Find the Factorial of a Number????

# In[1]:


a = int(input("Enter a number: ")) 
f = 1 
for i in range(1,a+1): 
	f = f * i 
 
print(f'The factorial of the number is {f}') 


# # Write a Python Program to Display the multiplication Table?

# In[2]:


num = int(input("Display multiplication table of? "))

for i in range (1,11):
    print (num, 'x', i, '=', num*i)


# # Write a Python Program to Print the Fibonacci sequence?

# In[6]:



def fibonacci(n):
    a = 0
    b = 1
     

    if n < 0:
        print("Incorrect input")
         

    elif n == 0:
        return 0
       
    
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
print(fibonacci(9))


# # 4. Write a Python Program to Check Armstrong Number?

# In[10]:


n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")


# # Write a Python Program to Find the Sum of Natural Numbers?

# In[9]:


# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
  
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




