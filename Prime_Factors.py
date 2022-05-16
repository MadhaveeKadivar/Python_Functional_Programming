'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 06:16:51
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 06:16:51
    @Title : Prime Factor
'''
def primefactors(number):
    """ 
        Description: 
            This function is calculating prime factors
        Parameter:
            It takes one integer argument 
        Return:
            returns set collection
    """
    prime_factors = set()
    if number % 2 == 0:
        prime_factors.add(2)
    while number % 2 == 0:
        number = number // 2
        if number == 1:
            return prime_factors
    for factor in range(3, number + 1, 2):
        if number % factor == 0:
            prime_factors.add(factor)
            while (number % factor == 0):
                number = number / factor
                if number == 1:
                    return prime_factors
# Taking input from user
number = int(input("\nEnter any number you want to prime factorize : "))
factors = primefactors(number) # Calling function
print(f"Prime factors of {number} are : ")
print(factors)