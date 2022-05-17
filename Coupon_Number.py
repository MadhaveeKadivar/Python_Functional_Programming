'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-14 09:48:15
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 09:48:15
    @Title : Coupon Number
'''
import random

def random_numbers(length):
    """ 
        Description: 
            This function is generating distinct digit coupon number
        Parameter:
            It takes total number of digits
        Return:
            number which have distinct digit
    """
    numbers_digits = []
    global count
    while len(numbers_digits) != length: #This loop continue till all the distinct numbers will cover
        random_number = random.randint(0,9) # Generating Random Number
        print(random_number)
        if random_number in numbers_digits: # checks if random number is already present in arry or not
            count += 1
            continue
        else:
            numbers_digits.append(random_number)# If present then remove this element from array
            count += 1   
    num = int("".join(map(str, numbers_digits)))
    return num
# Main Code
count = 0
total_distinct_number_digit = int(input("\nHow many digit numbers you want to generate as distinct coupon number : "))
number=random_numbers(total_distinct_number_digit)
print(f"\nDistinct digit coupon number is : {number}")
print(f"\nTotal random number needed to generate coupon number are : {count}")


