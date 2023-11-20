"List methods"
"list.append(item)"  # add item at end of list
"list.insert(index,item)"  # add item at index
"list.pop(index)"  # remove item at index
"list.remove(item)"  # remove item
"list.index(item)"  # search for index of item
"list.count(item)"  # get occurrences of item
"list.reverse()"  # reverse list
"list.sort()"  # sort list

"Traverse"  # Move through a sequence.
"Method"  # A function that belongs to an object.
"Custom  built function"  # A function that you have created yourself and imported into other programs that you have created.
"List"  # A dynamic data structure that holds items under one name. The items can be of varying data types.


# The list below contains string literals (i.e. pieces of text) and need to be in quotes
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet"]
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")
# What item is returned from the list and why?
print(f"{listOfNames[2]}\n")
# "SIlvia" is returned, as it's in index position number 2.

"Exercise:"
# You have been provided with the multidimentional list below.
"Your tasks are listed below"
# 1. Print the multidimentional list
# 2. Print Nicole, number 10 and JS
# 3. Print Laura, number 20 and Python
# 4. Print Juliet, number 50 and NoSQl

twoDLists = [
    #      0      1          2       3       4
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],  # 0
    # List of numbers
    [10, 20, 30, 40, 50],  # 1
    # List of Tecnologies
    ["JS", "Python", "HTML", "CSS", "NoSQL"],  # 2
]

#SOLUTUTIONS:
#1. Print the multidimentional list

twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

# Loop through each list in the two-dimensional list
for i in range(len(twoDLists)):
    # Loop through each element in the inner list
    for j in range(len(twoDLists[i])):
        print(twoDLists[i][j], end="\t")  # Use \t for tab spacing
    print()  # Move to the next line after printing each inner list



# 2. Print Nicole, number 10 and JS
twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

# Print specific elements
print(twoDLists[0][0])  # Nicole
print(twoDLists[1][0])  # 10
print(twoDLists[2][0])  # JS



# 3. Print Laura, number 20 and Python
twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

# Print specific elements
print(twoDLists[0][1])  # Laura
print(twoDLists[1][1])  # 20
print(twoDLists[2][1])  # Python


# 4. Print Juliet, number 50 and NoSQl
twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

# Print specific elements
print(twoDLists[0][4])  # Juliet
print(twoDLists[1][4])  # 50
print(twoDLists[2][4])  # NoSQL

"Reasearch Nested for loop"
print("Nested for loop..........")
# Can you use a nested for loop to loop through the multidimensional list ?
#Answser: YES!
twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

print("Nested for loop..........")

# Loop through each list in the two-dimensional list
for i in range(len(twoDLists)):
    # Loop through each element in the inner list
    for j in range(len(twoDLists[i])):
        print(twoDLists[i][j], end="\t")  # Use \t for tab spacing
    print()  # Move to the next line after printing each inner list


"Reasearch enumerate"
print("Nested for loop with enumerate..........")
# Can you use a nested for loop and enumerate through the multidimensional list?
#Answser: YES!
twoDLists = [
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],
    [10, 20, 30, 40, 50],
    ["JS", "Python", "HTML", "CSS", "NoSQL"],
]

print("Nested for loop with enumerate..........")

# Loop through each list in the two-dimensional list
for i, inner_list in enumerate(twoDLists):
    # Loop through each element in the inner list
    for j, element in enumerate(inner_list):
        print(f" {i},{j}: {element}")


# The enumerate object yields pairs containing a count
# (from start, which defaults to zero) and a value yielded by the iterable argument.


"Practice exercise over the weekend"
# Create a shopping list program

def display_menu():
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from shopping list")
    print("4. Clear shopping list")
    print("5. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def remove_item(shopping_list):
    view_list(shopping_list)
    if shopping_list:
        try:
            index = int(input("Enter the item number to remove: ")) - 1
            removed_item = shopping_list.pop(index)
            print(f"{removed_item} removed from the shopping list.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid item number.")
    else:
        print("Shopping list is empty.")

def clear_list(shopping_list):
    shopping_list.clear()
    print("Shopping list cleared.")

def shopping_list_program():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            view_list(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            clear_list(shopping_list)
        elif choice == "5":
            print("Exiting the shopping list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    shopping_list_program()
