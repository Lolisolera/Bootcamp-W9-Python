# SUBROUTINE

def userName():
    name = "Fredddy"
    print(name)

    # call/invoque the subroutine
    userName()



    # Exercise: modify the code above in tne subroutine to ask for user input
    #instead of coded values.
def getUserName():
    name = input("Enter your name: ")
    return name

def printUserName():
    name = getUserName()
    print(f"Hello, {name}!")

# Call the subroutine to print the user's name
printUserName()

#--------------------------

def addition():
    answer =2+10
    print(f"THe answer to 2 +10 is {answer}")


# addition() # call/invoque the subroutine

# Exercise: # addition() # call/invoque the subroutine
#MOdify to code above to use variables for the numbers
#added with the input function

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} is {answer}")

# Call the subroutine
addition()



# Exercise: Modify the code above by changing subroutine name to
#subtraction, multiply or division to perform the respective operation


def subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")

def multiplication():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")

def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Check for division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")

# Call the respective subroutines
# Uncomment the line corresponding to the operation you want to perform

addition()
#subtraction()
#multiplication()
# division()


#----------------------------
#Exercise: Modify the code below to use parameters(arguments)
#Define a subroutine called username
"""
def username():
    first_name = "Firstname"
    last_name = "last name"
    interests = "interests"
print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")
"""

#Solution:

def username(first_name, last_name, interests):
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")

# Call the function with specific values
username("Firstname", "Lastname", "Interests")




#-----

#Fuctions are more useful as we can reuse the variable that we got back
# subroutine is jsut to be used one off.

# task: modify the code above and turn it into a function.
# Have a return value from it. 

def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    interests = input("Enter your interests: ")
    return first_name, last_name, interests

def print_user_info():
    first_name, last_name, interests = get_user_info()
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")

# Call the function to print user information
print_user_info()
