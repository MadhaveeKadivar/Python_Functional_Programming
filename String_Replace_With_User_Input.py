'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 3:22:37
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 3:22:37
    @Title : User Input
'''
def greet(username):
    """ 
        Description: 
            This function is checking that year is leap year or not
        Parameter:
            It takes username(string) as argument
        Return:
            returns true or false
    """
    str = "Hello "+username+" , How are you?"
    return str
while(True):
    username = input("Enter your name : ")
    if(len(username)>3):
        break
    print("Usename have minimum 3 character")
str = greet(username)
print(str)