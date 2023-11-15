#FOR LOOPS:

# using start, stop, step, create a count-down program:

import time

def countdown(start, stop, step):
    for i in range(start, stop, step):
        print(f"Countdown: {i}")
        time.sleep(1)  # Pause for 1 second

    print("count down!")


countdown(11, 0, -1)


#TASK 1

# Complete the code below to iterate through both lists, add comment to explain your code 

highscore = [125, 63, 35, 12]
#"block of code is missing here"

for score in highscore: # Iterate through the highscore list

    print(score)  # Print each score

usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]
#"block of code is missing here"
for user in usersList: # Iterate through the usersList
    print(user)   # Print each user


#TASK2 
# Debug and fix the multiplication program below 
# add comment where you fix the bugs

print("Welcome to the table quiz.\n")
num = int(input("Enter a number: "))


for i in range(1, 11): #Use range to define the range of values for i in the loop
     # Indent the following lines to be inside the loop
    answer = int(input(f" What is {i} x {num}? "))
    print(f"the answer is {answer} ")

      # Fix: Calculate the correct answer inside the loop
       
    correct = i * num

    if answer == correct:
        print("Correct")
    else:
        print(f"No, the answer is {correct}")
  


#--------------------------------



