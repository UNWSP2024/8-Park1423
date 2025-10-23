##
# Code by: Parker Jolly
# On: 10/23/2025
# Program name: Initials
##

def initials_generator(personsName):
    personsInitials = ""

    # Iterate through and add uppercase letters to the initials
    for char in personsName:
        if char.isupper():
            personsInitials += char + "."
    
    return personsInitials.strip()

# Get input and output initials
personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)