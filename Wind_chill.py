'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 06:36:02
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-15 06:36:02
    @Title : Wind chill
'''
# importing math and sys module
import math
import sys
def find_wind_chill(t, v): 
    """ 
        Description: 
            This function is calculating wind chill
        Parameter:
            It takes two integer value one is for temperature and second is for wind speed
        Return:
            wind chill
    """   
    windchill = 35.74 + 0.6215*t + (0.4275*t - 35.75)*(math.pow(v,0.16))
    return windchill
# Taking input from user
# temp = int(input("\nPlease enter temperature value in fahrenheit : "))
# wind_speed = int(input("\nPlease enter wind speed in miles per hour : "))
#Command Line Argument
temp = int(sys.argv[1])
wind_speed = int(sys.argv[2])
if temp <= 50 and (wind_speed <= 120 or wind_speed >= 3): #Checking condition
    windchill = find_wind_chill(temp, wind_speed) # Calling function
    print("\nwind chill is: ", windchill)
else:
    print("\nRequired Temperature value is less than 50 and wind speed is less than 120 or greater than 3")
