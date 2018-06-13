
# coding: utf-8

# In[7]:




def tile_cost_calculator():
    
    try:
        w = int(input("Enter the width of the floor in metres"))
        h = int(input("Enter the height of the floor in metres"))
        c = int(input("Enter the cost of covering the floor with tiles per sq.m in INR"))
    
    #area in sq.m
    
        total_area = w*h
    
    # cost in INR
    
        total_cost = total_area *  c
    
        print("%s INR is the total cost of covering the floor"%(total_cost))
    
    except:
    
        print("Please enter appropriate values")
    


# In[8]:


tile_cost_calculator()

