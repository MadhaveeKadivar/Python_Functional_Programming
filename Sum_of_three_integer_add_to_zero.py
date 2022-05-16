'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 04:02:03
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-14 04:02:03
    @Title : Sum of three integer add to zero
'''
# Importing module of array
import array as arr

def find(arr, n):  
    """ 
        Description: 
            This function is finding triplets where sum of three integer add to zero
        Parameter:
            It takes array of integer and size of array as argument
        Return:
            returns list of triplets
    """ 
    list = []
    for i in range(0, n-2):              
        for j in range(i+1, n-1):           
            for k in range(j+1, n):               
                if (arr[i] + arr[j] + arr[k] == 0): 
                   # print(arr[i], arr[j], arr[k]) 
                    tuple_items = (arr[i],arr[j],arr[k])
                    list.append(tuple_items)
    return list  
# Taking number from user and add to array
a = arr.array('i', [])
n = int(input("\nEnter how many numbers you want to add in array : "))
for i in range(n):
    no = int(input(f"Enter {i} th number : "))
    a.append(no)
# Calling function
result = find(a, n)
print(f"\nTotal Number of triplets : {len(result)}")
print(f"\nList of triplets are : {result}")
