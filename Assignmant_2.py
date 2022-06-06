#!/usr/bin/env python
# coding: utf-8

# # 1. What are the two values of the Boolean data type? How do you write them?
# 
# Ans:- The boolean can only carry  two values: true and false (Boolean literals). Boolean expressions use relational and logical operators. The result of a Boolean expression is either true or false. like 0 and 1 .

# # 2. What are the three different types of Boolean operators?
# 
# Ans:- There are three basic Boolean search commands: AND, OR and NOT. 

# # 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# Ans:- 
# con:-1        con:2     NOT     AND     OR
# false	      false     true	false	false
# false	      true	    true	false	true
# true	      false	    false	false	true
# true	      true	    false	true	true

# #  4. What are the values of the following expressions?

# In[1]:


(5 > 4) and (3 == 5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


#   # 5. What are the six comparison operators?
#   
# Ans:- Python contains six comparison operators, which are written below:
# 
# 1:-Less than (<)
# 
# 2:-Less than or equal to (<=)
# 
# 3:-Greater than (>)
# 
# 4:-Greater than or equal to (>=)
# 
# 5:-Equal to (==)
# 
# 6:-Not equal to (!=)

# # 6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.
# 
# Ans:- The difference between the equal to and assignment operators ia shown below:-
# 
# 1:- Assignment (=) :- The “=” is an assignment operator is used to assign the value of variable.
# 
# a=23
# b=56
# c=76
# d=57
# 
# a+b+c+d
# 
# 
# 2:- Equal to (==):- The ‘==’ operator is use to check two given operands are equal or not. If so, it returns true. Otherwise it returns false.
# 
# 4==4 = True
# 7==6 = False

# # 7. Identify the three blocks in this code:

# In[5]:


spam = 0
if spam == 10:
    print('eggs')


# In[6]:


if spam > 5:
    print('bacon')
else:
    print('ham')


# In[7]:


print('spam')
print('spam')


# # 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[8]:


spam==1
print ('Hello')
if spam == 2:
    print ('howdy')
else:
        print ('Greetings')


# # 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# 
# Ans: We can stop endless loop by pressing "CTRL + C". we can also use "break" statement  in our code to stop this type of loop.

# # 10. How can you tell the difference between break and continue?
# 
# Ana:- The basic difference is; break keyword terminates the rest of remaining iterations of the loop. On the contrary, the continue keyword terminates only the current iteration of the loop.

# # 12. 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[9]:


for i in range(1, 11):
    print(i)


# In[10]:


i = 1
while(i<=10):
    print(i)
    i += 1


# # 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# Ans:- spam.bacon().
