import unittest
from app import validate_input

class TestValidation(unittest.TestCase):
    
    def test_valid_input(self):
        result = validate_input("John", "Doe", "1234567890", "New York", "123456")
        self.assertEqual(result, "Valid input")
    
    def test_invalid_first_name(self):
        result = validate_input("John123", "Doe", "1234567890", "New York", "123456")
        self.assertEqual(result, "Invalid first name")

    def test_invalid_mobile(self):
        result = validate_input("John", "Doe", "12345", "New York", "123456")
        self.assertEqual(result, "Invalid mobile number")
    
    def test_invalid_city(self):
        result = validate_input("John", "Doe", "1234567890", "New York123", "123456")
        self.assertEqual(result, "Invalid city")
    
    def test_invalid_pincode(self):
        result = validate_input("John", "Doe", "1234567890", "New York", "12345")
        self.assertEqual(result, "Invalid pincode")

if __name__ == '__main__':
    unittest.main()

