"""
Welcome to Appointment Maker.
-------------------------------------------------------------------------------
Automate the inputing of appointment data all into one easy to use script.
===============================================================================
Information needed:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1. Name of Union Member
2. Name of Union 
3. Date of Birth
4. Telephone, H=Home, C=Cellphone
5. Email Address, Must contain valid name@emailservice.com format
6. Address
7. Name of Primary Beneficiary
8. Name of Contingent Beneficiary
9. A section for any additional notes.
10. Date of Appointment
11. Time of Appointment
12. Name of file.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
After info is submitted, program will store info as a .txt file in a directory
labeled APPOINTMENTS. 
"""
print("Welcome to Appointment Maker!")
date = input("Please enter a date for appointment: ")
time = input("What time is the appointment? ")
union_member = input("What is the name of the union member? ")
birthdate = input("What is the union member's date of birth: mm/dd/yy ")
telephone = input("What is the union member's primary telephone# ")
email = input("What is the union member's email address? ")
home_address = input("What is the union member's mailing address? ")
primary_beneficiary = input("Who is the union member's primary beneficiary: ")
contingent = input("Who is the contingent beneficiary ")
# folder = "C:\Users\ianbt\Desktop\Appts"
