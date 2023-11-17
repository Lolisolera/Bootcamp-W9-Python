# SUBROUTINE
"""
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

def username():
    first_name = "Firstname"
    last_name = "last name"
    interests = "interests"
print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")


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



# ------------
# TIM's solution
def get_user_info(fullName, address, interests):
    para = f"my name is{fullName}, my address is {address} and my interests are {interests}"
    return para

sentence = userName4("Bob", "Kingston", "Reggae")
print(sentence)


#-------------------

def addition(pNum1, pNum2, *args):

    answer = pNum1 + pNum2

    print(args)

    for value in args:
        print(value)

        return args
    

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter first second: "))


# 3 fields are optional

if len(args) ==1:
    print(args[0])

#print(additional(num1, num2))

print(addition1(4, 5, "Name", "Fruit", "Drink", "4", "7.5", "True"))


"MOdify the code above to use args(arguments)"

"""


# PYTHON GAMES/APPS

#1. Create a Fibonacci App using Python:

def fibonacci(n):
    fibSequence = [0, 1]

    for i in range(2, n):
        nextNum = fibSequence[-1] + fibSequence[-2]
        fibSequence.append(nextNum)

    return fibSequence[:n]

# Get user input for the number of Fibonacci numbers to generate
numTerms = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate and print the Fibonacci sequence
result = fibonacci(numTerms)
print("Fibonacci Sequence:", result)




# 2.ASK THE USER FOR A NUMBER AND CHECK WHETER THE NUMBER IS PRIME OR NOT:

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
userInput = input("Enter a number: ")

# Check if the input is a valid integer
try:
    userNumber = int(userInput)
    if isPrime(userNumber):
        print(f"{userNumber} is a prime number.")
    else:
        print(f"{userNumber} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
