#FOR LOOPS APPS AND GAMES:
"""
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

      # Calculate the correct answer inside the loop
       
    correct = i * num

    if answer == correct:
        print("Correct")
    else:
        print(f"No, the answer is {correct}")


print("Finished")
  
"""
#--------------------------------


# TASK 3
#Complete the code below to display multiplication table of your choice
num1 =int(input("Enter number for multiplication: "))
#'block of code is missing here"
"""
1 x 5 = 5
2 x 5 = 
3 x 5 = 
4 x 5 = 
5 x 5 = 
6 x 5 = 
7 x 5 = 
8 x 5 = 
9 x 5 = 

""" 


# SOLUTION TASK 3:
num1 = int(input("Enter number for multiplication: "))

# Display multiplication table for num1
for i in range(1, 13):
    result = i * num1
    print(f"{i} x {num1} = {result}")


#----------------------------------------------

#Extension Task:
#Build a program that iterates through a word given by the user 
# and returns whether each letter is a consonant or a vowel.


word = input("Enter a word: ").lower()

# Iterate through each letter in the word
for letter in word:
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

print("Finished")

