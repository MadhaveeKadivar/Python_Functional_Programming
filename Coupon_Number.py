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
            This function is generating random numbers to cover all the distinct coupon number present in list
        Parameter:
            It takes number of distinct numbers
        Return:
            List of distinct coupon numbers
    """
    distinct_coupon_numbers = []
    global count
    while True: #This loop continue till all the distinct numbers will cover
        random_number = random.randint(0,100) # Generating Random Number
        if random_number in distinct_coupon_numbers: # checks if random number is already present in arry or not
            continue
        else:
            distinct_coupon_numbers.append(random_number)# If present then remove this element from array
        count += 1
        if len(distinct_coupon_numbers) == length:          
            break            
    return distinct_coupon_numbers
count = 0
total_distinct_numbers = int(input("\nHow many numbers you want to generate distinct coupon numbers : "))
list_of_distinct_numbers=random_numbers(total_distinct_numbers)
print(f"\nDistinct coupon number are : {list_of_distinct_numbers}")
print(f"\nTotal random number needed to have all distinct numbers are : {count}")


