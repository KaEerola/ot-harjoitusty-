import unittest
from src.services.validation_service import validate_inputs
from datetime import date

class TestValidation(unittest.TestCase):

    def test_valid(self):
        result = validate_inputs("Kytäjä", "72", "2026-04-13")
        self.assertEqual(result, ("Kytäjä", 72, "2026-04-13"))

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_inputs("Kytäjä", "abc", "2026-04-13")

    def test_negative_score(self):
        with self.assertRaises(ValueError):
            validate_inputs("Kytäjä", "-5", "2026-04-13")
    
    def test_empty_course(self):
        with self.assertRaises(ValueError):
            validate_inputs("", "72", "2026-04-13")
    
    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            validate_inputs("Kytäjä", "72", "13-04-2026")
    
    def test_empty_date(self):
        result = validate_inputs("Kytäjä", "72", "")
        self.assertEqual(result[2], date.today().isoformat())