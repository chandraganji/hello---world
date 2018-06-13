
# coding: utf-8

# In[20]:


#Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzbuzz(n):
    
    a = [x for x in range(0,n+1)]
    
    
    def replace_item(i):
        
        if i%3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        
        elif i % 5 == 0:
            return 'Buzz'
        
        elif i%3 == 0:
            return 'Fizz'
        else:
            return i
        
    for item in map(replace_item,a):
        
        print (item)
    
    
    
    
        
    
    


# In[21]:


fizzbuzz(100)

