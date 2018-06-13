
# coding: utf-8

# In[13]:


def reverse_string(x):
    
    a = x.split()
    
    b = a[::-1]
    
    c = ' '.join(b)
    
    print (c)


# In[14]:


reverse_string("hello how")

