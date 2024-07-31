import unittest
from unittest.mock import patch, MagicMock
from personnel import Employee
from personnel import Driver
from logs import Logger

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(
            first_name="Jane",
            last_name="Smith",
            employee_id=1,
            salary=12000.00,
            license_number="LIC1001",
            qualifications=["BLS"]
        )

    def test_initialization(self):
        self.assertEqual(self.driver.first_name, "Jane")
        self.assertEqual(self.driver.last_name, "Smith")
        self.assertEqual(self.driver.employee_id, 1)
        self.assertEqual(self.driver.salary, 12000.00)
        self.assertEqual(self.driver.license_number, "LIC1001")
        self.assertEqual(self.driver.qualifications, ["BLS"])

    def test_str(self):
        expected_str = (
            "Driver ID: 1, Name: Jane Smith, Salary: 12000.00 zł, "
            "License Number: LIC1001, Qualifications: BLS"
        )
        self.assertEqual(str(self.driver), expected_str)

    @patch.object(Logger, 'debug')
    def test_update_salary(self, mock_debug):
        self.driver.update_salary(13000.00)
        self.assertEqual(self.driver.salary, 13000.00)
        mock_debug.assert_called_with("Updated salary: 13000.00")

if __name__ == '__main__':
    unittest.main()
