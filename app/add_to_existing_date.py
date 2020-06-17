print("Welcome to Appointment Maker!")
print("======================================================================")
date = input(
    "What is the date of the appointment you're adding to?" 
    "eg(weekday-day.txt): ")
time = input("What time is the appointment: eg(12PM) ")
union_member = input("What is the name of the union member? ")
union_name = input("What is the name of the union? ")
birthdate = input("What is the union member's date of birth? mm-dd-yy ")
telephone = input(
    "What is the union member's primary telephone? eg(111-222-3333) ")
email = input("What is the union member's email address? ")
home_address = input("What is the union member's mailing address? ")
primary_beneficiary = input("Who is the union member's primary beneficiary? ")
contingent = input("Who is the contingent beneficiary? ")
child_safe_kit = input("How many Child Safe Kits were ordered? ")
# folder = "C:\Users\ianbt\Desktop\Appts"

filename = date
with open(filename, "a") as f_obj:
    f_obj.write("----------------------------------------------------------\n")
    f_obj.write(f"Time: {time}\n")
    f_obj.write(f"Name: {union_member}\n")
    f_obj.write(f"Date of Birth: {birthdate}\n")
    f_obj.write(f"Telephone: {telephone}\n")
    f_obj.write(f"Email: {email}\n")
    f_obj.write(f"Address: {home_address}\n")
    f_obj.write(f"Beneficiary: {primary_beneficiary}\n")
    f_obj.write(f"Contingent Beneficiary: {contingent}\n")
    f_obj.write(f"Child Safe Kits: {child_safe_kit}\n")
    f_obj.write("----------------------------------------------------------\n")
