
# coding: utf-8

# In[9]:


'''
This code aims to find out the country where the IP address is registered.

Uses ipgetter and ipstack

'''
#finding external ipaddress

import ipgetter
import requests
import json

def findip_country():
    
    my_ip = format(ipgetter.myip())
    
    #finding the details of server
    
    ipstackapi_base_url = 'http://api.ipstack.com/'+my_ip
    accesskey_ipstack = '7d46ff1b21f40f4b2d1e99e9e3b93188'
    parameters_ipstack = {'access_key':accesskey_ipstack}
    response_ipstack = requests.get(url = ipstackapi_base_url,params = parameters_ipstack)
    country_data = response_ipstack.json()
    #print(city_data)
    
    print("___________________________________________________________________")
    print("Your ip address is: {}".format(my_ip))
    print("Details of your external server location")
    print("------------------------------------------")
    print("Latitude of your server location is: {}".format(country_data["latitude"]))
    print("Longitude of your server location is: {}".format(country_data["longitude"]))
    print("IP address of your server is: {}".format(my_ip))
    print("Name of the location is {} which is located in {}".format(country_data['city'],country_data['country_name']))
    






# In[10]:


findip_country()

