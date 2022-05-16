'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-14 05:32:11
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-14 05:32:11
    @Title : Gambler problem
'''
import random
total_bets = win = lose=0    
def gambling(stake,goal):
    """ 
        Description: 
            This function is used for betting 1 rupees until itsreached to the goal amount or lose all amount
        Parameter:
            It takes two integer argument one as stake amount and other as goal amount
        Return:
            returns True if win or False if lost
    """
    amount = stake
    global total_bets,win,lose      
    while(stake >0 and stake != goal):
        bet = random.randint(0,1)
        if(bet==1):
            print("Wins 1 Rupee")
            stake += 1
            win += 1
        else:
            print("Lose 1 Rupee")
            stake -= 1
            lose += 1
        total_bets += 1
    if stake == goal :
        return True
    else:
        return False
while True:    
    stake = int(input("Enter stake amount : "))
    goal = int(input("Enter goal amount : "))
    #no_of_times = int(input("Enter number of time to continue this game : "))
    if(stake > 0 and goal > 0):
        break
    else:
        print("Stake amount and goal amount should not be less than 0")        

result = gambling(stake,goal) #Calling function
print(f"\nInitial Stake amount = {stake}")
if result:
    print("\n\nGambler Won!!!")
    print(f"\nCurrent Stake amount = {goal}")
else:
    print("\n\nGampler Lost!!!")
    print(f"\nCurrent Stake amount = 0")
print(f"\nTotal number of bets made = {total_bets}")
print(f"Total number of won : {win}")
print(f"Total number of lost : {lose}")
win_percentage = (win/(total_bets))*100
lose_percentage = (lose/(total_bets))*100
print(f"Wins Percentage : {win_percentage}")
print(f"Lose Percentage : {lose_percentage}")