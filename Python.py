#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Understanding the variables in Python:
Rules for declaring the variables in python:
Rule no. 1: No namespace while Declaring  the Variable name
Rule no. 2: A variable name should never start with a number
Rule no. 3: A variable name should not contain any special characters(@#$%^&*)


# In[ ]:





# In[ ]:


Introduction to datatypes:
1.	Strings-> str
2.	Numbers(Intergers => int & Floats [Decimals =>0.1 ,0.2]) == float
3.	Lists => list
4.	Tuples => tuple
5.	Dictionaries => dict
Classification of Datatypes:
Broadly Datatypes are classified into 2 categories:
1.	Mutable Datatypes => which we can edit / alter => flexible in nature
2.	Imutable Datatypes => which we cannot  edit / alter => fixed in nature
Introduction to string datatype:
Definition: A string is nothing but a series of characters declared in quotes.
Classification it is classified as an immutable datatype
How to define the string datatype:
1. Single quotes
2. Double quotes


# In[1]:


Introduction to String methods:


# In[4]:


name="Mustafa"
name2="Mustafa2"
type(name)
type(name2)


# In[5]:


fullname = "joseph anthony"
print(fullname)
print(fullname.title())
#req: i want the entire name in capitals...
print(fullname.upper())
#req: i want the entire name in small case letters...
print(fullname.lower())



# In[ ]:


continuation with strings :
understanding the concept of f strings :


# In[ ]:


# Genral syntax of f strings :
f"custom message {placeholder -1} {placeholder-2}... {placeholder...N}"


# In[1]:


firstname = "pradeep"
lastname = "kumar"
#req: i want to get the full name.....?
fullname = f"{firstname} {lastname}"
print(fullname)
print(fullname.title())
message = f"keep up the good work, {fullname.title()}"
print(message)


# In[2]:


Adding whitspace to strings:


# In[ ]:


print("Programming_languages:PyhtonJavaC++C")


# In[ ]:


#\n -------------> Printing the code on next line


# In[ ]:


print("Programming_languages:\nPyhton\nJava\nC++\nC")


# In[ ]:


#\t -------------> Printing the code After tabbing


# In[ ]:


print("Programming_languages:\n\tPyhton\n\tJava\n\tC++\n\tC")


# In[ ]:


Removing blank space from the string:


# In[9]:


name="      Python"
name1="Pyhton         "
name2="Python"
name3="        Python          "
print(name+"\n"+name1+"\n"+name2)
name.lstrip()
name1.rstrip()
name3.strip()


# In[ ]:




