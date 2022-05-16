'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 5:24:56
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 5:24:56
    @Title : Harmonic Number
'''
def harmonic(number):
    """ 
        Description: 
            This function is calculating harmonic value of nth number
        Parameter:
            It takes one integer as argument
        Return:
            Harmonic value
    """
    result = 0
    for i in range(1,number+1):
        result += (1/i)
    return result
number = int(input("\nEnter number you want find Harmonic Value upto this : "))
value = harmonic(number) #Calling Function 
print(f"\n{number}th harmonic value is : {value}")