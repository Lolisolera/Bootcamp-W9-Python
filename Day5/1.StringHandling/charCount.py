searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")

"iterate over a string to find an count a character"

# we set count to the value of zero
count = 0
# Iterate through the entire string to search for the character
for char in searchStr:
    # Check if the character entered matches any character in the string
    if char == findChar:
        # Increase the count by 1 every time a match is found
        count += 1

# Display the result
print(f"The character '{findChar}' appears {count} times in the string.")

#-------------------------------------------------------------------------

# Exercise: refactor the code above by putting it into a subroutine and invoke it

def count_character(search_str, find_char):
    count = 0
    for char in search_str:
        if char == find_char:
            count += 1
    return count

searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")

result_count = count_character(searchStr, findChar)

print(f"The character '{findChar}' appears {result_count} times in the string.")
