'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 06:02:58
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-15 06:02:58
    @Title : Roots of given Quadratic Equation 
'''
# importing math module
import math

def find_roots(a, b, c):
    """ 
        Description: 
            This function is finding roots of Quadratic Equation
        Parameter:
            It takes three numeric value as argument
        Return:
            Nothing
    """
    delta = b * b - 4 * a * c
    sqrt_delta = math.sqrt(abs(delta))
 
    if delta > 0:
        print(f"Real root 1 : {(-b + sqrt_delta)/(2 * a)}")
        print(f"Real root 2 : {(-b - sqrt_delta)/(2 * a)}")
    elif delta == 0:
        print(f"Only one real root : {-b / (2*a)}")
    else:
        print(f"Complex root 1 : {- b / (2*a)} + i{sqrt_delta/ (2 * a)}")
        print(f"Complex root 2 : {- b / (2*a)} - i{sqrt_delta/ (2 * a)}")

# Taking input from user
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(f"Quadratic equation : ({a})x^2 + ({b})x + {c}")
# Calling function
find_roots(a, b, c)