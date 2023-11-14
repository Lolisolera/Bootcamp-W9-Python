"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=  not equal to
"""

# https://www.w3schools.com/python/python_operators.asp

# if statement: write what is the same and different to JS

#differences in syntax, indentation, and additional features
#reflect the unique characteristics of each programming language.

#JS 
# if (condition) {
# code to be executed if the condition is true

#Python
#if condition:

#in Python the INDENTATION is new

""""
SAME:
- if keyword
- if is followed by a condition
- block of code that is run if condition is true
 
DIFFERENT:
- no () containing the condition
- : instead of { to indicate where the code block to be executed is
- code block is not encased inside {}
- code block is indented, which is not necessary in js (although it is advised)
 
everything I had
"""

""""
SAME:
- if keyword
- if is followed by a condition
- block of code that is run if condition is true
 
DIFFERENT:
- no () containing the condition
- : instead of { to indicate where the code block to be executed is
- code block is not encased inside {}
- code block is indented, which is not necessary in js (although it is advised)
 
everything I had
"""

# Exercise: Using if and else
   
# Create a program that finds the minimum value between two numbers

"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 < num2:
    minimum = num1
else:
    minimum = num2

print("The minimum value between", num1, "and", num2, "is:", minimum)


# using if else


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 < num2:
    result_message = "The minimum value is: " + str(num1)
else:
    result_message = "The minimum value is: " + str(num2)


print(result_message)

"""

# tasks:
## Exercise modify the code above to use the OR & NOT logical operator

#Fix the Code
 
"""
cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit to users inputs
if 
  # King == User Input      and   Hearts    == User Input  
    print("Winner!")
else:
    print("Try Again")

"""

#SOLUTION:
"""
cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit to users inputs
if chkCardValue == cardvalue and chkCardSuit == suitOfcards:
    print("Winner!")
else:
    print("Try Again")

"""



"""
# Extension Exercise (may require some additional independent research!!):
# 1) Use if else to find item from a list

subjects = ["Math", "English", "Computers"]
choice = int(input("choose one subject:"))

if subjects[choice] == subjects[0]:
   print(f"You've chosen{subjects[choice]}")
   print(subjects[choice] == subjects[0])

else:
   print("That didn't match")   
   print(subjects[1])
   print(choice)
   


# 2) print the index value if the item is found
# 3) otherwise print a message "item not in list/not found"

""" 






#--------------------------------------------------------------------------

"""
SELECTION:
In Python, these are the types of selection statements:
if.
if-else.
if-elif-else.
"""


""""
# Exercise: Using if Elif and else
# Create a Menu program that allows user to select between three subject choices

print("Subject Menu:")
print("1. Music")
print("2. Maths")
print("3. English")
print("4. Exit")


choice = input("Enter the number of the subject you want to choose (or enter 4 to exit): ")

if choice == "1":
    print("You selected Music.")
elif choice == "2":
    print("You selected Maths.")
elif choice == "3":
    print("You selected English.")
elif choice == "4":
    print("Exiting the program. Goodbye!")
else:
    print("Invalid choice. Please enter a number between 1 and 3.")


# User must be presented with the value associated with each choice
# for example 1. Music, 2. Maths ....

# A choice must also be available for the user to exit the program

# A message using the print function must be display as per the user choice

# Check the user's choice and display the corresponding message

"""







#TASK 2: LEAP YEAR:

# LEAP YEAR is when  a year is divisible by 4 but not by 100, or is divisible by 400.

#Try to build a program that figures out whether a given year is a leap year or not. 
# You will need to use .format(year) in your code, so you may want to research what it does first.

"""

year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

"""

#Task:
#Create a age verification system that checks a users age for restricted products being purchased.
#Include a nested if else statement for the verification process.


userAge = int(input("Enter your age: "))

minAge = 18


if userAge >= minAge:
    print("Age verification successful. What vaping flavour would you like to buy?")
    
    confirmation = input("Do you want to proceed with the purchase? (yes/no): ").lower()
    
    # Nested if-else for purchase confirmation
    if confirmation == "yes":
        print("Thank you for your purchase!")
    elif confirmation == "no":
        print("Purchase canceled.")
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
else:
    print("Sorry, you are not eligible to purchase vaping products. Age verification failed.")

