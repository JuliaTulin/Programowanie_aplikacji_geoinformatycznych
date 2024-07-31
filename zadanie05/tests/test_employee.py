import unittest
from unittest.mock import patch, MagicMock
from logs import Logger
from personnel import Employee

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee(
            first_name="John",
            last_name="Doe",
            employee_id=1,
            salary=5000.00
        )

    def test_initialization(self):
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.employee_id, 1)
        self.assertEqual(self.employee.salary, 5000.00)

    def test_str(self):
        self.assertEqual(
            str(self.employee),
            "Employee ID: 1, Name: John Doe, Salary: 5000.00 zł"
        )

    @patch.object(Logger, 'debug')  # Zamieniamy Logger.debug na MagicMock
    def test_update_salary(self, mock_debug):
        self.employee.update_salary(6000.00)
        
        # Sprawdzamy, czy salary zostało zaktualizowane
        self.assertEqual(self.employee.salary, 6000.00)
        
        # Sprawdzamy, czy Logger.debug został wywołany z odpowiednim komunikatem
        mock_debug.assert_called_with("Updated salary: 6000.00")

if __name__ == '__main__':
    unittest.main()
