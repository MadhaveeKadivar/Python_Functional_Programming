'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-13 3:30:46
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 3:30:46
    @Title : Flip Coin
'''
# Importing random module
import random
# Declaring variables
heads=tails=0

def flip_coin(numer_of_flips):
    """ 
        Description: 
            This function is flipping coin and count heads and tails
        Parameter:
            Number of flips 
        Return:
            Nothing
    """
    global heads ,tails
    for i in range(1,number_of_flips+1):
        result = random.random()
        print(f"\n\nCoin filpping for {i} times ......")
        if(result < 0.5):
            print("\nCoin flipping Result : Tails")
            tails += 1
        else:
            print("\nCoin flipping Result : Heads")
            heads += 1
            
number_of_flips=int(input("\nEnter number of times you want to flip coin : "))
# Flipping coin 
flip_coin(number_of_flips) # calling function
# Calculating Percentage
h = (heads/(number_of_flips))*100
print(f"\n\nHeads Percentages after fliping coin {number_of_flips} times  : {h} % ")
print(f"\nTails Percentages after fliping coin {number_of_flips} times  : {100-h} %")