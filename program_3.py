##
# Code by: Parker Jolly
# On: 10/23/2025
# Program name: Capital Quiz
##

import random

quiz_material = {
    "Minnesota":"St. Paul",
    "Florida":"Tallahasse",
    "Utah":"Salt Lake City",
    "New Jersey":"Trenton",
    "New Mexico":"Santa Fe",
    "New York":"Albany",
    "North Carolina":"Raleigh",
    "North Dakota":"Bismarck",
    "Ohio":"Columbus",
    "Oklahoma":"Oklahoma City",
    "Oregon":"Salem",
    "Pennsylvania":"Harrisburg"
}

def main():
    # Keep quizzing while we have material
    while len(list(quiz_material.items())) >= 1:
        
        # Select a random item from the list and then remove it
        current_question = random.choice(list(quiz_material.items()))
        quiz_material.pop(current_question[0])

        # Get input
        answer = input("What is the capital of " + str(current_question[0] + "? "))

        # Display correct or incorrect message
        if check_answer(answer,current_question[1]):
            print("Correct!")
        else:
            print("Thats incorrect. The correct answer is " + current_question[1] + ".")



def check_answer(answer,correct_answer):
    # Compare answer and correct_answer after making both lowercase and removing periods and spaces.
    return (answer.lower().replace(" ","").replace(".","")
             == 
             correct_answer.lower().replace(" ","").replace(".",""))
        

if __name__ == "__main__":
    main()