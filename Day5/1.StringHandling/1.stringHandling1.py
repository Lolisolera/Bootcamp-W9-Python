"""You can perform operations with string in a similar way to the operations 
that you can perform with numbers. """
compareLetters = "a" > "b"  # check if the letter a is greater than b
print(compareLetters)

town= "York"
city = "york"
print(town == city) #False, Capital letter - ASCII Table 

compareLetters = "b" > "a"  # check if the letter b is greater than a
print(compareLetters)

"You can multiply a string, it will concatenate the same value for the number of times stated."
mutiplyWord = "Python\n" * 5  # mulitply the word n times
print(mutiplyWord) #TimTimTimTimTim

"""The + sign concatenates (joins) the two string together.
There is no space because it hasn't been given that instruction"""
joinWords = "Python" + " " + "Java"  # join the two words
print(joinWords)
"Exercise"
# Create two variables fName and lName and join and print them using a variable called fullName
fName = "Lola"
lName = "Marquez"

# Joining fName and lName to create fullName
fullName = fName + " " + lName

# Print the fullName
print(fullName)



"You can also use string-handling techniques to find out things about a string.  "
"""
len() is used to count the number of characters in a string.
This would include spaces as well if they were present.
In Python, the index always starts at 0.

# """
course = "Python"
wordlength = len(course) #6
print(wordlength)  # returns the length of the string

# How can we find/print a specific character in a word or string in a list?
# "Python"[0]
findFirstLetter = course[0]  # returns the first character from the string "Python"
print(findFirstLetter)

"Exercise"
# Return all the characters from the string held in the course variable using negative values

# [-6:] 
course = "Python"

# Return all characters using negative indices
all_characters = course[-6:]
print(all_characters)

# the negative values start counting from "-1" and from the end of the word or sentence, eg:
# Python
# 012345

# negative value -6 is the letter "P"

#[0:]
course = "Python"

# Return all characters using positive indices
all_characters = course[0:]
print(all_characters)


# How can you access the letter h?

course = "Python"

# Access the letter 'h' using positive index
letter_h = course[3]
print(letter_h)


"Exercise:"
#  use any comparison operator to compare the letter "a" and "A"

# Comparing the letters 'a' and 'A'
result = 'a' == 'A'

# Print the result
print(result)

# The output of the above code is FALSE, as their ASCII numbers are different FOR LOWER CASE AND CAPITAL A.

#  use any comparison operator to compare the letters "ax" and "ZZ"
# Comparing the strings "ax" and "ZZ"
result = "ax" < "ZZ"

# Print the result
print(result)
# The output in the above code is TRUE, as the  lexicographical order, "ax" comes before "ZZ". 


#  use any comparison operator to compare your firstname with any another first name
# != , == , <= , >=, <,>

fName1 = "Lola"
fName2 = "Paul"

not_equal = fName1 != fName2 

print("Not Equal:", not_equal)


"For further reading See Python documentation for other string methods"
# https://docs.python.org/3.3/library/stdtypes.html?highlight=substring#string-methods
"""swapcase()
capitalize()
endswith()
find() 
isnumeric()
isdigit()
isdecimal()
"""


programme = "Match of the Day"
#            0123456789 h[10] e[11] space[12] D[13] a[14] y[15]
# 
print(programme[0]) #M
print(programme[-1]) #y
print(programme[-9]) #f
print(programme[-9:]) #[start:end], f the Day
print(programme[-16:]) #[start:end], Match of the Day





