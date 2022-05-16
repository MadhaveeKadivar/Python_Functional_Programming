'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 06:58:39
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-15 06:58:39
    @Title : String Permutation
'''
def find_factorial(n):
    """ 
        Description: 
            This function is finding factorial of integer number
        Parameter:
            It takes one integer as argument
        Return:
            returns factorial value
    """
    fact = 1
    if (n == 0 or n == 1):
        return 1
    else:
        for i in range(1,n+1):
            fact = fact * i
    return fact

def PermutationsUsingIterative(str):
    """ 
        Description: 
            This function is generating string permutation using Iterative method
        Parameter:
            It takes string as argument
        Return:
            returns list of all permutations
    """
    n = len(str)
    permutations_iteration = []
    no_of_permutations = find_factorial(n); 
    for i in range(no_of_permutations):
        chars = list(str)        
        temp = i
        div = n
        s = ""
        while div >= 1:            
            quotient = int(temp/div)
            remainder = int(temp%div)
            s = s + chars[remainder]
            chars.remove(chars[remainder])            
            temp = quotient
            div -= 1
        permutations_iteration.append(s)
    return permutations_iteration


list_recursive = []
def PermutationsUsingRecursion(s,ans):
    """ 
        Description: 
            This function is generating string permutation using Recursive method
        Parameter:
            It takes string as argument
        Return:
            returns list of all permutations
    """
    global list_recursive
    if(len(s) == 0): 
        list_recursive.append(ans)
        return
    for i in range(len(s)):
        c = s[i]
        left = s[0:i]
        right = s[i+1:]
        result = left + right
        PermutationsUsingRecursion(result, ans+c)

# Main Code 
str = input("Enter any string : ")
list_iterative = PermutationsUsingIterative(str)
print(list_iterative)
PermutationsUsingRecursion(str,"")
print(list_recursive) 

if(list_iterative == list_recursive):
    print("\nList of string permutations returned both function is Equal\n")
else:
    print("\nList of string permutations returned both function is not Equal")