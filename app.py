import re

def validate_input(first_name, last_name, mobile_number, city, pincode):
    # Validate first name and last name (only letters, spaces allowed)
    if not re.match("^[A-Za-z ]+$", first_name):
        return "Invalid first name"
    if not re.match("^[A-Za-z ]+$", last_name):
        return "Invalid last name"
    
    # Validate mobile number (10 digits)
    if not re.match("^[0-9]{10}$", mobile_number):
        return "Invalid mobile number"
    
    # Validate city (only letters and spaces allowed)
    if not re.match("^[A-Za-z ]+$", city):
        return "Invalid city"
    
    # Validate pincode (6 digits)
    if not re.match("^[0-9]{6}$", pincode):
        return "Invalid pincode"
    
    return "Valid input"

