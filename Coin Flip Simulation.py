
# coding: utf-8

# In[3]:


import random

def coin_flip():
    
    possible_flip_outcomes = ('Heads','Tails')
    
    n = int(input("No.of times you want to flip the coin?  "))
    
    actual_outcomes = []
    
    for i in range(1,n+1):
        
        actual_outcomes.append(random.choice(possible_flip_outcomes))
    

    print("No.of heads is equal to  %s" %(actual_outcomes.count("Heads"))) 
    
    print("No.of tails is equal to  %s" %(actual_outcomes.count("Tails")))
    
    print("The list of actual outcomes is %s" % actual_outcomes)
    
    


        
        
        
        
        
    
    
    
    
    
    


# In[4]:


coin_flip()

