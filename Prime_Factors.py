'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 06:16:51
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 06:16:51
    @Title : Prime Factor
'''
def primefactors(no):
    """ 
        Description: 
            This function is calculating prime factors
        Parameter:
            It takes one integer argument 
        Return:
            returns set collection
    """
    prime_factors = set()
    if no % 2 == 0:
        prime_factors.add(2)
    while no % 2 == 0:
        no = no // 2
        if no == 1:
            return prime_factors
    for factor in range(3, no + 1, 2):
        if no % factor == 0:
            prime_factors.add(factor)
            while (no % factor == 0):
                no = no / factor
                if no == 1:
                    return prime_factors
# Taking input from user
num = int(input("\nEnter any number you want to prime factorize : "))
factors = primefactors(num) # Calling function
print(f"Prime factors of {num} are : ")
print(factors)