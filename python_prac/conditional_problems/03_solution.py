# **************************************** GRADE CALCULATOR ****************************************

try:
    # Asking user to enter their marks and converting input to an integer
    user_marks = int(input("Enter your marks: "))

    # Checking if the marks entered are invalid (100 or more)
    if user_marks >= 100:
        print("Verify your marks again")  # Asking the user to recheck their marks
        exit()  # Exiting the program

    # Grade classification based on the user's marks
    if user_marks >= 90:  
        print("Congrats, your grade is A")  # Marks 90 or above → Grade A
    
    elif user_marks >= 80:  
        print("Congrats, your grade is B")  # Marks 80-89 → Grade B

    elif user_marks >= 70:  
        print("Congrats, your grade is C")  # Marks 70-79 → Grade C

    elif user_marks >= 60:  
        print("Congrats, your grade is D")  # Marks 60-69 → Grade D

    else:  
        print("You have failed")  # Marks below 60 → Fail

except ValueError:
    # Handling invalid input (if the user enters a non-numeric value)
    print("Enter valid marks.")
