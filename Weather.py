
# coding: utf-8

# In[17]:


'''
This code is designed to generate the details of weather conditions of your place based on the your

external IP address.

We shall use following api's in this code

a) ipstack, for getting the geo location of your position based on the ip address
b) openweather, for getting the weather conditions based on the geo location.

'''

#importing all the libraries
#importing ipaddress from ipgettter library and converting it to text.
import requests
import json
import ipgetter

def get_weather():
    my_ip = format(ipgetter.myip())
    
    ipstackapi_base_url = 'http://api.ipstack.com/'+my_ip
    accesskey_ipstack = '7d46ff1b21f40f4b2d1e99e9e3b93188'
    parameters_ipstack = {'access_key':accesskey_ipstack}
    response_ipstack = requests.get(url = ipstackapi_base_url,params = parameters_ipstack)
    geo_data = response_ipstack.json()
    #print(geo_data)
    print("___________________________________________________________________")
    print("Details of your external server location")
    print("------------------------------------------")
    print("Latitude of your server location is: {}".format(geo_data["latitude"]))
    print("Longitude of your server location is: {}".format(geo_data["longitude"]))
    print("IP address of your server is: {}".format(my_ip))
    print("Name of the location is {} which is located in {}".format(geo_data['city'],geo_data['country_name']))
    
    
    openweather_base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    accesskey_openweather = 'c8d3bb841290fff3c644806201a32c11'
    parameters_openweather = {'lat':geo_data["latitude"],'lon':geo_data["longitude"],'APPID':accesskey_openweather,'units':'metric'}
    response_openweather = requests.get(url = openweather_base_url,params = parameters_openweather)
    weather_data = response_openweather.json()
    #print(weather_data)
    print("____________________________________________________________________________________")
    
    print("Please find the details of weather condition at the this location mentioned below")
    print("------------------------------------------------------------------------------------")
    print("Weather condition is: {}".format(weather_data['weather'][0]['main']))
    print("Temperature currently reported in deg C is:{}".format(weather_data['main']['temp']))
    print("Atomspheric pressure in hPa is:{} ".format(weather_data['main']['pressure']))
    print("Humidity is {}".format(weather_data['main']['humidity']))
    print("Minimum temp. in deg C at the moment is:{}".format(weather_data['main']['temp_min']))
    print("Maximum temp. in deg C at the moment is:{}".format(weather_data['main']['temp_max']))
    print("Wind speed in meter/sec is:{}".format(weather_data['wind']['speed']))
    print("Direction of wind in degrees is:{}".format(weather_data['wind']['deg']))
    print('\n\n')
    print("Thanks!")
    
    


# In[18]:


get_weather()

