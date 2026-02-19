# here we make a program where the system works according to the number of attempts 
import time

max_retries = 5
attempts = 0                                                            
wait_time = 1

while attempts < max_retries:
    print("Attempts ",attempts+1, "wait time = ",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
