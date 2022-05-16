'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 3:30:46
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 4:12:34
    @Title : Leap Year
'''
def leap_year(year):
    """ 
        Description: 
            This function is checking that year is leap year or not
        Parameter:
            It takes one integer as argument
        Return:
            returns true or false
    """
    if ((year%4)==0 and (year%100)!=0 or (year%400)==0):
        return True 
    else:
        return False
    
while(True):
    year = int(input("\nEnter any 4 digit Year : "))
    if (year > 1000  and  year < 9999):
        break
    print("\nPlease enter only 4 digit year")
    
result = leap_year(year) # Calling function
if(result):
    print(f"\n{year} is a Leap Year")
else:
    print(f"\n{year} is not Leap Year")