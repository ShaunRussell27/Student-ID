# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:31:07 2024

@author: shaun
"""

print("Student services")
while True:
    option=input("Pick an Option Student or adminstrator [S or A]")
    if option.lower()=='s':
        def getRandomStr():
            import random
            # This will generate a random 6-digit string
            random_string = ''.join(random.choices("0123456789", k=6))
            #return the code to the function
            return random_string


        code=getRandomStr()
        d1, d2, d3, d4, d5, d6 = map(int, code)



        #b
        def calcCheckDigit():
            # Calculate check digit using the formulacheck_digit
            check_digit = ( d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6* d6) % 10
            check_digit=str(check_digit)
            return check_digit



        digit=calcCheckDigit()



        #C
        def generateStudentId():
            #While statement allowing the user to enter the college until correct input
            while True:
                campus=input("What campus do you go to ([M],[D],[G],[S])")
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
                    
            String="ATU"
            String += campus.upper()
            String += code
            String += digit
            print(f"This is your student ID: {String}")
            return String
            
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
     #For adminstrator       
    elif option.lower()=='a':
        #creates student IDS same as before
        def CreateStudentId():
            import random
            # This will generate a random 6-digit string
            random_string = ''.join(random.choices("0123456789", k=6))
            #will do the math
            d1, d2, d3, d4, d5, d6 = map(int, random_string)
            check_digit = ( d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6* d6) % 10
            check_digit=str(check_digit)
            #creates top part of ID
            while True:
                campus=input("What campus do you go to ([M],[D],[G],[S])")
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
            #forms all together      
            String="ATU"
            String += campus.upper()
            String += random_string
            String += check_digit
            print(String)
            return String
        # a diferent valid student Id for adminstrator
        def validateStudentId(stu,the_list):
            #allows validatestudeNTID to accept an ID
            import re
            # Define the regex pattern for validation
            pattern = r"^ATU[GMSD]\d{7}$"
            #checks length of string
            length=len(stu)
            #checks if ID is already in the list
            if stu in the_list:
                return False#returns false if is in list
            else:
                #Checks both of the nessacities
                if length==11 and re.match(pattern,stu):
                    return True#returns true if meets criteria
                else:
                    return False#false if doesnt
                
            
        def register_students():
            #Registers new students and adds their unique IDs to a list
            registered_ids = []  # List to store student ID
            print("\nStudent Registration System")
            #creation of ID or add to the list
            #creates ID to add to list
            while True:
                # Prompt for user 
                option = input("\nCreate[c] or add to a list [a] (or type 'END' to quit): ").strip().lower()

                if option == 'end':  # Terminate registration process
                    print("\nRegistration complete.")
                    break
                elif option == 'c':  # Create new IDs and add to the list
                    while True:
                        stop = input("\nPress Enter to create and add an ID, or type 'END' to stop: ").strip()
                        if stop.upper() == "END":
                            print("\nStopped creating IDs.")
                            break
                
                        # Generate and add a new student ID
                        student_id = CreateStudentId()
                        registered_ids.append(student_id)
                        print(f"New Student ID: {student_id}")
                        
                #allows adminstratot to add id manually
                elif option == 'a':  # Manually add IDs to the list
                    while True:
                        ID = input("\nEnter a valid Student ID (or type 'END' ): ").strip()
                        if ID.upper() == "END":
                            print("\nStopped adding IDs.")
                            break
                
                        # Validate and add the student ID
                        if validateStudentId(ID,registered_ids):
                            registered_ids.append(ID)
                            print(f"New Student ID: {ID}")
                        else:
                            #if entry is invalid or ID already exists
                            print("\nInvalid entry or the ID is already present. Please try again.")
                else:
                    print("\nInvalid entry")
                
            #Displays list
            print("\nFinal List of Registered Student IDs:")
            for sid in registered_ids:
                print(sid)
                
            return registered_ids#returns list
                
        
            # Run the registration function
        #register_students()
        
        def get_students_by_campus(student_ids, campus):
            # Map campus names to their corresponding letters for the fourth character
            campus_map = {
                "Donegal": "D",
                "Mayo": "M",
                "Sligo": "S",
                "Galway": "G"
            }
        
            # Get the corresponding letter for  campus
            campus_letter = campus_map.get(campus, "").upper()
        
            # Filter IDs where the fourth character matches  campus letter
            filtered_ids = [sid for sid in student_ids if len(sid) > 3 and sid[3] == campus_letter]
            return filtered_ids
                
        
        if __name__ == "__main__":
            # Register students and retrieve the list of IDs
            registered_ids = register_students()
    
        # Reporting: List IDs by campus
        while True:
            print("\nReport Generation")
            #allows user to enter campus they want to find
            campus = input("Enter campus name either (Donegal, Galway, Mayo, Sligo) or 'END' to exit: ").strip()
        
            if campus.upper() == "END":
                print("Exiting report generation.")
                break
            
            # Validate campus input
            valid_campuses = ["Donegal", "Galway", "Mayo", "Sligo"]
            if campus not in valid_campuses:
                #If entered incorrectly
                print("Invalid campus name. Please enter another valid campus.")
                continue
    
            # Filter and display student IDs for the campus
            campus_ids = get_students_by_campus(registered_ids, campus)
            print(f"\nNumber of students in {campus}: {len(campus_ids)}")
            print("\nStudent IDs:")
            #Display list
            for sid in campus_ids:
                print(sid)
            
           
            
    else:
        print("Invalid Entry")
