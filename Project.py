# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:32:02 2024

@author: shaun Russell
"""



#A
#Method that creates the 6 random numbers as a string
def getRandomStr():
    import random
    # This will generate a random 6-digit string
    random_string = ''.join(random.choices("0123456789", k=6))
    #return the code to the function
    return random_string


#create a map variable of random string for the check digit function
code=getRandomStr()
d1, d2, d3, d4, d5, d6 = map(int, code)



#b
# calccheck digitfunction uses the map of each integer from previous function
def calcCheckDigit():
    # Calculate check digit using the formulacheck_digit
    check_digit = ( d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6* d6) % 10
    #change back to a string
    check_digit=str(check_digit)
    #return code to the function
    return check_digit


#create variable
digit=calcCheckDigit()



#C
def generateStudentId():
    #While statement allowing the user to enter the college until correct input
    while True:
        campus=input("What campus do you go to ([M],[D],[G],[S])")
        #allows both capitals and non capitals inputs
        if campus.lower() =='d':
            print("Donegal has been picked")
            break;
        elif campus.lower() =='m':
             print("Mayo has been picked")
             break;
        elif campus.lower() =='g':
             print("Galway has been picked")
             break;
        elif campus.lower() =='s':
             print("Sligo has been picked")
             break;
        else:
            print("Invalid entry")
            
    #String is created from previous variables
    String="ATU"
    String += campus.upper()
    String += code
    String += digit
    #string is displayed
    print(f"This is your Studen ID:  {String}")
    #return code to the function
    return String
    

#creates variable of final string
check=generateStudentId()



#D
def validateStudentId():
    
    #allows validatestudeNTID to accept an ID
    import re
    # Define the regex pattern for validation
    pattern = r"^ATU[GMSD]\d{7}$"
    inp=input("Please enter your student ID:")
    #checks length of string
    length=len(inp)
    
    #Checks both of the nessacities
    if length==11 and re.match(pattern,inp):
        print("valid student ID")
    else:
        print("invalid student ID")
        
       
#Ask the user if they want to validate their student ID or not
validate=input("Do you want to check if student ID is valid [Y/n]")       
if validate.lower() == 'y':
    #call the last function
    validateStudentId()
else:
    print("Student ID was not validated")