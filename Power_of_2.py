'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 5:02:33
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 5:02:33
    @Title : Power of 2
'''
def power(number):
    """ 
        Description: 
            This function is calculating any power of 2
        Parameter:
            It takes one integer as argument
        Return:
            Nothing
    """
    result = 1
    for i in range(1,number+1):
        result *= 2
        print(f"\n2 ^ {i} = {result}")
# User Input   
number = int(input("\nEnter number you want to Find power of 2 : "))
power(number)# Calling function