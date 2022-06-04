#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# 
# *= Sign of multiplication (mathematical operators)
# 
# 'hello' = String
# 
# -87.8 = Float
# 
# - = Sign of subtraction (mathematical operators)
# 
# / = Sign of subtraction (mathematical operators)
# 
# + = Sign of addition (mathematical operators)
# 
# 6 = Integer

#  # What is the difference between string and variable?
# 
# The major difference between string and variaable is : A variable is used to store the input that could hold a number, an array, a set, a string or even a function.
# 
# On the other hand, a string variable is used to store string values i.e. a stream of characters.
#     

# # Describe three different data types
# 
# A data type, is a classification that specifies which type of value a variable has and what type of mathematical, relational or logical operations is associated with it.
# 
# 
# 
# 1:-Integer (int); It is the most common numeric data type used to store numbers without a fractional component such as 44, 23, 1, 0.
# 
# 2:-Floating Point (float); It is also a numeric data type used to store numbers that may have a fractional component such as 557.34, 33.4, -23.34.
# 
# 3:-String (str or text); It is a sequence of characters and the most commonly used data type to store text such as "mannu" , "ineuron" etc.
# 

# # What is an expression made up of? What do all expressions do?
# 
# An expression is a combination of operators and operands to produce desired value. In any programming language, an expression is evaluated as per the precedence of its operators.
# 
# # eg:
# 
# a = 10 + 1.3
#   
# print(a)
# 
# output:- 11.3
# 
# Expressions are used to evaluate the values or represent the result on the screen

# # This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# Expression is made up of values, containers, and mathematical operators (operands) and the statement is just like a command that a python interpreter executes like print.

# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# In[2]:


bacon = 22
bacon +1


# # What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'
# 
# 'spam' * 3

# In[3]:


'spam' + 'spamspam'


# In[4]:


'spam' * 3


# # Why is eggs a valid variable name while 100 is invalid?
# 
# The only reason behind it is we can't start variable with an integer name. if we, we should begin with, a string-like alphabet name then integer is valid
# 
# for eg:- e100, eggs100

# # What three functions can be used to get the integer, floating-point number, or string version of a value?
# 
# str()
# int()
# float()

# # Why does this expression cause an error? How can you fix it?
# 
# 'I have eaten' + 99 + 'burritos' 
# 
# The only reason behind it is 99 is an integer it cannot be concatenated with strings.
# to solve this type of problem we have to do typecasting.
