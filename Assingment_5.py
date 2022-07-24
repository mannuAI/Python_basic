#!/usr/bin/env python
# coding: utf-8

# # Write a Python Program to Find LCM?

# In[1]:


def calculate_lcm(x, y):  
      
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  

num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  

print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2)) 


# # Write a Python Program to Find HCF?

# In[3]:


def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)


# # Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[7]:


dec= 220

print ("the decimal value of", dec, "is:")
print (bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# # Write a Python Program To Find ASCII value of a character?

# In[10]:


ASCII_Value='M'

print("The ASCII value of input is", ord(ASCII_Value))


# # Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[ ]:


def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[ ]:




