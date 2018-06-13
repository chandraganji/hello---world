
# coding: utf-8

# In[5]:


from pygeocoder import Geocoder
import numpy as np
import sys

#radius of earth in kilometres

R = 6731

def get_distance(locA,locB):
    
    '''
    distance calculation based on Harvesine Formula.
    
    '''
    
    dlon = np.deg2rad(locB[1]) - np.deg2rad(locA[1])
    dlat = np.deg2rad(locB[0]) - np.deg2rad(locA[0])
    a = (np.sin(dlat/2))**2 + (np.cos(np.deg2rad(locA[0]))) * (np.cos(np.deg2rad(locB[0]))) * (np.sin(dlon/2))**2
    c = 2 * np.arctan2((a**0.5),((1-a)**0.5))
    d = R * c
    return d

def get_coordinates(location):
    
    #function to export coordinates in the format (lat,log)
    
    
    results = Geocoder.geocode(location)
    return results[0].coordinates
    
def distance():
    
   
    
    #names of the two cities being taken from user based on the which distance is calculated
    
    
    first_city = input("Please enter the name of the first city   ")
    second_city = input("Please enter the name of the second city ")
    final_distance = get_distance(get_coordinates(first_city),get_coordinates(second_city))
    final_distance = get_distance(first_city,second_city)
    return final_distance
    print("The distance between %s and %s in Kilometres is %s." %(first_city,second_city,final_distance))
    

    #Whether user requires the distance in different units?
    

    
    units_change = input("Do you want to have the distance calculated in  different units? Y or N  ")
    
    if units_change.lower()[0] == 'y':
        
        user_choice = input("Please pick one from the options miles and metres for conversion   ")
        
        if user_choice.lower() == 'miles':
            
            final_distance_miles = final_distance * 0.61
            
            print("The distance in miles is %s."%(final_distance_miles))
        
        else: 
            
            final_distance_metres = final_distance * 1000
            
            print("The distance in metres is %s."%(final_distance_metres))
    else:
        
        print ("Thanks for using the app!")

    
        
    
    
    



