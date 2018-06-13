
# coding: utf-8

# In[6]:


def palindrone(x):
    
    
    try:
        if x == x[::-1]:
            print("Yes!The string that is supplied is a plaindrone")
        else:
            print("No! The string that is supplied is not a plaindrone")
        
    except:
        print("Please enter appropriate values")
        
    else:
        print("Thanks")
        
        


# In[9]:


palindrone(123)

