
# coding: utf-8

# In[7]:


def vowelcount(x):
    from collections import Counter
    counter = Counter(x)
    print("The no.of a's in the string are :{} Nos".format(counter['a']))
    print("The no.of e's in the string are :{} Nos".format(counter['e']))
    print("The no.of i's in the string are :{} Nos".format(counter['i']))
    print("The no.of o's in the string are :{} Nos".format(counter['o']))
    print("The no.of u's in the string are :{} Nos".format(counter['u']))
    print("Total no.of vowels in the string are: {} Nos".format(counter['a']+counter['e']+counter['i']+counter['o']+counter['u']))
    
    


# In[8]:


vowelcount("Hello, My name is Chandra")

