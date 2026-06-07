# Age Calculator - Using Functions
from datetime import datetime

def get_dob():
    dob = input("\nEnter Your DOB [YYYY-MM-DD]: ")
    return dob
        
def validate_dob(dob):
    try:
        dob_data = datetime.strptime(dob, "%Y-%m-%d")
        return dob_data
    except ValueError:
        print("Invalid DOB! The DOB You Just Enter is Incorrect.")
        return None
                

def calculate_age(dob_data):
    dob_year = dob_data.year
    dob_month = dob_data.month
    dob_date = dob_data.day
        
    this_year = datetime.now().year
    this_month = datetime.now().month
    today = datetime.now().day

        
    if (this_month, today) >= (dob_month, dob_date):
        age = this_year - dob_year

    else:
        age = this_year - dob_year - 1

    return age

print("="*36 + " STARTED " + "="*35)
    
while True:

    try:
        
        # Main Program
        dob = get_dob()
        dob_data = validate_dob(dob)

        if dob_data:
            age = calculate_age(dob_data)
            print(f"\nYou are {age} years old.")
            
        else:
           print("Please Enter a Valid DOB Again.")
           continue

        print("\n" + "="*80)
        print("-" * 27 + " Coded By : Basant Jangra " + "-" * 27)
        print("="*80 + "\n\n")
        
    except KeyboardInterrupt:
        print("\n\nProgram Closed by User.")
        break
    except ValueError:
        print("\n\nInvalid Value! Only Numbers and Hypen are Allowed.")
        continue
    
