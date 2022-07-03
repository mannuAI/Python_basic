#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to convert kilometers to miles?

# In[1]:


Kilometers= float(input("Enter the value in Kilometers: "))

# conversion factor

conv_fac = 0.621371
miles = Kilometers * conv_fac

print ('%0.2f Kilometers is equal to %0.2f miles' %(Kilometers,miles))


# # Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


celsius_2 = float (input("Temperature value in degree Celsius: " ))  
Fahrenheit_2 = (celsius_2 * 9/5) + 32   
print ('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius_2, Fahrenheit_2))  


# # Write a Python program to display calendar?

# In[3]:


import calendar
yy=2022
mm=7
print (calendar.month(yy,mm))


# # Write a Python program to solve quadratic equation?

# In[4]:


import math 
 
print('I will solve the equation ax^2+bx+c=o') 
 
a = int(input('a= ')) 
b = int(input('b= ')) 
c = int(input('c= ')) 
 
d = b**2-4*a*c 
 
if d < 0: 
   print('The equation has no real solution') 
elif d == 0: 
   x = (-b)/(2*a) 
   print('This equation has one solution: ',x) 
else: 
   x1 = (-b+math.sqrt(d))/(2*a) 
   x2 = (-b-math.sqrt(d))/(2*a) 
   print('This equation has two solutions: ',x1, 'or', x2) 


# # Write a Python program to swap two variables without temp variable?

# In[5]:


x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:




