##
# Code by: Parker Jolly
# On: 10/23/2025
# Program name: Course Info
##
courses = {}

def main():
    
    while True:
        # Have user give first input and if its 0, break, otherwise get the second input and add them to courses
        input1 = input("Enter the course ID (e.g. COS 2005) or 0 to exit: ")
        if input1 == "0":
            break
        else:
            input2 = input("Enter the course name: ")
            courses.update({input1:input2})
    
    while True:
        # Get input and break if 0
        input1 = input("Enter a course subject (e.g. COS) or 0 to exit: ")
        if input1 == "0":
            break
        
        # Print courses with the subject we want
        print("These are the courses with that subject:")

        for key in courses:
            # If the first 3 letters of the key are the same as our input, print that key pair
            if key[:3].lower() == input1.lower().strip():
                print(str(key) +": " + str(courses.get(key)))

if __name__ == "__main__":
    main()