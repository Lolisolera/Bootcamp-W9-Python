"Use chr() and ord() to perform ASCII conversions"

# Performing ASCII conversions in Python​
# Python has two functions that perform ASCII conversions: ​
# chr(97):This takes a decimal number and returns its character equivalent. ​
# ord("a"):This takes a character and returns its decimal equivalent. ​


aChar = input("Enter a character: ")
# ord takes a character and returns its decimal equivalent
convertChar = ord(aChar)
print(convertChar)


userMsg = "Message"
number = int(input("Enter number: "))
convertNum = chr(number)
secretMsg = userMsg + convertNum
print(secretMsg)


# chr(97):This takes a decimal number and returns its character equivalent. ​

"""Exercise: Complete the code block below to print a list of converted numbers to letter as specified in the range, the 
questions marks indicates where the code is missing"""
# def alphabets(): # created the function alphabets

def alphabets(start, end):
    # Ensure the range is within valid ASCII values for uppercase and lowercase letters
    start = max(start, 65)
    end = min(end, 122)

    # Create an empty list to store the converted letters
    alphabet_list = []

    # Loop through the range and append the corresponding letters to the list
    for num in range(start, end + 1):
        alphabet_list.append(chr(num))

    return alphabet_list

# Call the function with the desired range
result_list = alphabets(65, 75)

# Print the resulting list
print(result_list)
