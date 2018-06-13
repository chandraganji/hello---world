
# coding: utf-8

# In[16]:


try:
    n = int(input("Please enter the number till which you require the sequenc to be fibonnachi?"))
    def fibon(n):
        a = 1
        b = 1
        for i in range(n):
            yield a 
            a,b = b,a+b
    for number in fibon(n):
        print(number)
        
except:
    print("Please enter correct value!")

