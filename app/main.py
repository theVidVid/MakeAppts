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
date = input("What is the date of the appointment? eg(weekday-day.txt): ")
time = input("What time is the appointment? eg(12PM): ")
union_member = input("What is the name of the union member? ")
union_name = input("What is the name of the union? ")
birthdate = input("What is the union member's date of birth? mm-dd-yy ")
telephone = input(
    "What is the union member's primary telephone? "
    "eg(111-222-3333): "
)
email = input("What is the union member's email address? ")
home_address = input("What is the union member's mailing address? ")
primary_beneficiary = input("Who is the union member's primary beneficiary? ")
contingent = input("Who is the contingent beneficiary? ")
child_safe_kit = input("How many Child Safe Kits were ordered? ")

filename = f"{date}"

with open(filename, "w") as f_obj:
    f_obj.write("----------------------------------------------------------\n")
    f_obj.write("----------------------------------------------------------\n")
    f_obj.write(f"Time: {time}\n")
    f_obj.write(f"Name: {union_member}\n")
    f_obj.write(f"Union Name: {union_name}\n")
    f_obj.write(f"Date of Birth: {birthdate}\n")
    f_obj.write(f"Telephone: {telephone}\n")
    f_obj.write(f"Email: {email}\n")
    f_obj.write(f"Address: {home_address}\n")
    f_obj.write(f"Primary Beneficiary: {primary_beneficiary}\n")
    f_obj.write(f"Contingent Beneficiary: {contingent}\n")
    f_obj.write(f"Child Safe Kits: {child_safe_kit}\n")
    f_obj.write("----------------------------------------------------------\n")
