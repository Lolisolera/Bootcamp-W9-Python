#FOR LOOPS:

# using start, stop, step, create a count-down program:

import time

def countdown(start, stop, step):
    for i in range(start, stop, step):
        print(f"Countdown: {i}")
        time.sleep(1)  # Pause for 1 second

    print("count down!")


countdown(11, 0, -1)


# TIM'S SOLUTION:

for findNumber in range(5, -1, -1):
    print(findNumber)
#5,4,3,2,1,0
