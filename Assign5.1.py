# PUP Grading System
# use Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example: Input grade: 87.6, Grade/Mark: 1.75, Description: Very Good

import math

def grade_system():
    gradef = float(input("Enter your Grade here:  "))
    return gradef

grade_func = grade_system()
grades = round(grade_func)

if grades >= 97 and grades <= 100:
        print("Grade/Mark(Description): 1.00 (Excellent)")
else: 
    if grades >= 94 and grades <= 96:
        print("Grade/Mark(Description): 1.25 (Excellent)")
    else:
        if grades >= 91 and grades <= 93:
            print("Grade/Mark(Description): 1.5 (Very Good)")
        else:
            if grades >= 88 and grades <=90:
                print("Grade/Mark(Description): 1.75 (Very Good)")
            else:        
                if grades >= 85 and grades <=87:
                    print("Grade/Mark(Description): 2.00 (Good)")
                else:
                    if grades >= 82 and grades <= 84:
                        print("Grade/Mark(Description): 2.25 (Good)")
                    else:
                        if grades >= 79 and grades <= 81:
                            print("Grade/Mark(Description): 2.5 (Satisfactory)")
                        else:    
                            if grades >= 76 and grades <= 78:
                                print("Grade/Mark(Description): 2.75 (Satisfactory)")
                            else:
                                if grades == 75:
                                    print("Grade/Mark(Description): 3.00 (Passing)")
                                else:
                                    if grades >= 65 and grades <= 74:
                                        print("Grade/Mark(Description): 5.00 (Failure)")
                                    else:
                                        if grades == 0:
                                            print("If your grade is 0 or empty/blank it is either: ")
                                            print("Grade/Mark(Description): Inc. (Incomplete)")
                                            print("Grade/Mark(Description): W (Withdrawn)")
                                            print("Grade/Mark(Description): D (Dropped)")
                                            