'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 04:26:47
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-14 04:26:47
    @Title : Euclidean Distance
'''
# Importing Math Module
import math
def distance(x,y):
    """ 
        Description: 
            This function is calculating Euclidean distance from the point(x,y) to the origin (0,0)
        Parameter:
            It takes x and y coordinate as argument
        Return:
            returns distance
    """
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
# Taking input from user
x = int(input("Enter x coordinate : "))
y = int(input("Enter y coordinate : "))
# Calling Function
result = distance(x,y)
print(f"\nEuclidean distance from the point ({x},{y}) to the origin (0,0) is : {result}")