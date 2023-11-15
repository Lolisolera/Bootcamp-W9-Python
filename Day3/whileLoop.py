"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
num = 1  # int(input("Enter number below 20: "))

while num <= 20: # while condition = True - then we keep looping
    print(f"The number is {num}")
    num += 1  # what is this doing ? increments num by 1 every loop

"Exercise: Modify the code above to countdown from 20"

# "solution"
print("\ncountdown from 20")
num = 20
while num >= 0:
    print(f"The number is {num}")
    num -= 1  # what is this doing ? decrements num by 1 every loop



#------------------------------------
"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
num = 1  # int(input("Enter number below 20: "))

userNum = int(input("Enter a number: ")) #8
while num <= 20:
    print(f"The number is {num}")

    if num == userNum:  # set the condition to exit the loop
        print("exiting the loop...")

        break

    num += 1  # what is this doing ?

print("we have broken the loop")



# Extension activity:

# import the datetime library/class/module
import datetime

print("Not using while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))

# study the output of the code above and the output in the while loop to answer

# What is the while loop doing?

# add comment to explain what you understand the"datetime.datetime.now().strftime("%H:%M:%S")"

# add comment to explain what you understand the 'end='
"""
 Python's print() function comes with a parameter called 'end. 
 By default, the value of this parameter is '\n', i.e. the new line character. 
"""

# add comment to explain what you understand the "\r""'
"""
The '\r' character is used to return the cursor to the beginning 
of the current line without advancing to the next line.
"""

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    # time.sleep(1)
    
