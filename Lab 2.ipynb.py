#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing regular expression library 
import re 


# In[4]:


#using re.match 
#to find the first occurrence of the letter 'I' in the string 
 
sentence1 = re.match (r'I', 'I am learning text analytics') 
print (sentence1) 


# In[5]:


#using re.match 
#to find the first occurrence of the letter 'v' in the string 
 
sentence2 = re.match (r'v', 'I am learning text analytics') 
print (sentence2) 


# In[8]:


#using re.match 
#to find the first occurrence of the letter 'am' in the string 
 
sentence3 = re.match (r'am', 'I am learning text analytics')
print (sentence3) 


# In[9]:


sentence4 = re.search(r'am','I am learning text analytics')  
print (sentence4)  


# In[10]:


sentence5 = re.search(r'am', 'I am learning text analytics and am enjoying it')  
print (sentence5)  


# In[11]:


sentence6 = re.findall(r'am', 'I am learning text analytics and am enjoying it')  
print (sentence6)  


# In[12]:


sentence7 = re.split(r'and', 'I am learning text analytics and am enjoying it')  
print (sentence7)  


# In[13]:


sentence8 = re.split(r'am', 'I am learning text analytics and am enjoying it')  
print (sentence8)  


# In[14]:


sentence9 = re.split(r'am', 'I am learning text analytics and am enjoying it', maxsplit=1) 
print (sentence9)  


# In[15]:


sentence9 = re.split(r'am', 'I am learning text analytics and am enjoying it', maxsplit=2) 
print (sentence9)


# In[16]:


sentence10 = re.split(r'am', 'I am learning text analytics, I am enjoying it and I am going to ace it', maxsplit=3) 
print (sentence10)


# In[17]:


sentence11 = re.sub(r'I', 'we', 'I like text analytics and I enjoy learning it') 
print (sentence11)


# In[18]:


sentence1 = re.findall (r'.', 'I am learning text analytics') 
print (sentence1)
 
# Each letter is selected including spaces


# In[19]:


sentence2 = re.findall (r'\w', 'I am learning text analytics')
print (sentence2)
 
# Each letter is selected excluding spaces


# In[20]:


sentence3 = re.findall (r'\w*', 'I am learning text analytics') 
print (sentence3)
 
# Each word is selected including spaces 


# In[21]:


sentence4 = re.findall (r'\w+', 'I am learning text analytics') 
print (sentence4)
 
# Each word is selected excluding spaces 


# In[22]:


sentence5 = re.findall (r'^\w+', 'I am learning text analytics') 
print (sentence5)
 
# First word is selected  


# In[23]:


sentence6 = re.findall (r'\w+$', 'I am learning text analytics') 
print (sentence6)
 
# Last word is selected


# In[24]:


sentence7 = re.findall (r'\w\w', 'I am learning text analytics') 
print (sentence7) 
 
# 2 consecutive characters are selected 


# In[25]:


sentence8 = re.findall (r'\b\w\w', 'I am learning text analytics') 
print (sentence8) 
 
# 2 consecutive characters in a string are selected 


# In[26]:


sentence9 = re.findall (r'@\w+', 'user@text.com.my, user@analytics.gov.my, user@textanalytics.edu.my')
print (sentence9) 
 
# Only the first word in the domain name is selected


# In[27]:


sentence10 = re.findall (r'@\w+.\w+','user@text.com.my, user@analytics.gov.my, user@textanalytics.edu.my')
print (sentence10)


# In[28]:


sentence11 = re.findall (r'@\w+.\w+.\w+', 'user@text.com.my, user@analytics.gov.my, user@textanalytics.edu.my')
print (sentence11)


# In[33]:


# Solution  
 
sentence12 = re.findall (r'@\w+.(\w+.\w+)','user@text.com.my, user@analytics.gov.my, u')
print (sentence12) 
 
# To display the type of domain 


# In[34]:


sentence13 = re.findall (r'\d{2}-\d{2}-\d{2}', 'Ahmad BIT(IS) 15-05-2001, Johnny BCS(SE) 20-08-2000')
print (sentence13) 
 
# To display the date in the format of dd-mm-yy 


# In[35]:


sentence14 = re.findall (r'\d{2}-\d{2}-\d{4}', 'Ahmad BIT(IS) 15-05-2001, Johnny BCS(SE) 20-08-2000')
print (sentence14) 
 
# To display the date in the format of dd-mm-yyyy 


# In[36]:


sentence15 = re.findall (r'\d{2}-\d{2}-(\d{4})', 'Ahmad BIT(IS) 15-05-2001, Johnny BCS(SE) 20-08-2000')
print (sentence15) 
 
# Only the year will be displayed 


# In[37]:


sentence16 = re.findall (r'[aeiouAEIOU]\w+', 'I have eight story books. I often read them in afternoon')
print (sentence16)
 
# A sequence that starts with a vowel followed by one o rmore characters are selected 	


# In[38]:


sentence17 = re.findall (r'\b[aeiouAEIOU]\w+', 'I have eight story books. I often read them in afternoon')
print (sentence17) 
 
# Only words that start with vowels are selected 


# In[39]:


sentence18 = re.findall (r'\b[^aeiouAEIOU\s]\w+', 'I have eight story books. I often read them in afternoon')
print (sentence18) 
 
# Only words that start with non-vowels are selected 


# In[40]:


sentence19 = re.split (r'[;,]', 'I have many story books, colouring books; I often read them in the afternoon.')
print (sentence19) 
 
# split the words based on the delimiters semi colon and 


# In[41]:


sentence20 = re.split (r'[;,\s]', 'I have many story books, colouring books; I often read them in the afternoon.')
print (sentence20) 
 
# split the words based on the delimiters semi colon, comma and space 


# In[42]:


sentence21 = re.sub (r'[;,]', '.', 'I have many story books, colouring books; I often read them in the afternoon.')
print (sentence21) 
 
# Substitute the delimiters semi colon and comma with fullstops


# In[ ]:




