'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-15 05:17:41
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-15 05:17:41
    @Title : Stopwatch
'''
import time
def stopwatch():
    """ 
        Description: 
            This function is calculating time elapsed between start and end
        Parameter:
            None
        Return:
            returns time elapsed
    """
    try:
        start_time=time.time()
        print("\nStopwatch has started")
        input("\nPress ctrl+C to exit the stopwatch ")        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nStopwatch has stopped")
        end_time=time.time()
        
    return round(end_time-start_time,2)
#calling function
time_elapsed = stopwatch()
print(f"\n\nThe time elapsed : {time_elapsed} secs\n")