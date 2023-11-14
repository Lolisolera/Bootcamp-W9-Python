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