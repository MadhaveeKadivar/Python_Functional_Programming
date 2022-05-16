'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 04:04:47
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 04:04:47
    @Title : 2D Array
'''
def array(rows,columns):  
    """ 
        Description: 
            This function is used for creating 2D array
        Parameter:
            It takes two integer argument one as number of rows and other as numbers of columns
        Return:
            returns 2D array
    """  
    arr=[]
    for i in range(rows):
        column_value = []
        for j in range(columns):
            value = int(input(f"Enter arr[{i}][{j}] value : "))
            column_value.append(value)
        arr.append(column_value)
    return arr
def print_array(arr):
    """ 
        Description: 
            This function is used for printing 2D array
        Parameter:
            It takes 2d Array as argument
        Return:
            Nothing
    """
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

rows = int(input("Enter number of rows : "))
columns = int(input("Enter number of columns : "))
