'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 04:26:47
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-14 04:26:47
    @Title : Euclidean Distance
'''
# Importing Math Module
import math
import sys
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
# x = int(input("Enter x coordinate : "))
# y = int(input("Enter y coordinate : "))
# Command Line Argument
x_coordinate = int(sys.argv[1]) 
y_coordinate  = int(sys.argv[2])
# Calling Function
result = distance(x_coordinate,y_coordinate)
print(f"\nEuclidean distance from the point ({x_coordinate},{y_coordinate}) to the origin (0,0) is : {result}")