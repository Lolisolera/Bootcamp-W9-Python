
name = input("Enter name: ").title()

if name:
    print(f"Welcome {name}")
else:
    print(f"Your name '{name}' is not in title case.")

exit()  # exit


# I've tested the above code and no matter what input type I enter, 
# the output is always a welcoming message with my name.
# BUT if I delete the .title() function for the first line, 
# the "else" statement is activated!!! WHY???

