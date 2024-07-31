import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from operations import Incident
from logs import Logger 

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestIncident(unittest.TestCase):

    def setUp(self):
        Incident._Incident__max_id = 0
        self.valid_location = (50.0, 19.0)
        self.invalid_location = (130.0, 200.0)
        self.incident1 = Incident(
            description="Fire in building",
            priority="High",
            reported_time=datetime.now(),
            reporter_info="John Doe",
            incident_location=self.valid_location
        )

    def test_init(self):
        self.assertEqual(self.incident1.description, "Fire in building")
        self.assertEqual(self.incident1.priority, "High")
        self.assertEqual(self.incident1.reporter_info, "John Doe")
        self.assertEqual(self.incident1.incident_location, self.valid_location)

    def test_eq(self):
        self.incident2 = Incident(
            description="Car accident",
            priority="Medium",
            reported_time=datetime.now(),
            reporter_info="Jane Smith",
            incident_location=self.valid_location
        )
        self.assertNotEqual(self.incident1, self.incident2)

    @patch.object(Logger, 'error', autospec=True)
    def test_invalid_location_logging(self, mock_logger_error):
        self.incident_invalid_location = Incident(
            description="Flooding",
            priority="Low",
            reported_time=datetime.now(),
            reporter_info="Alice Johnson",
            incident_location=self.invalid_location
        )
        mock_logger_error.assert_called_once_with(
            f"Incident Flooding ({self.invalid_location}) - Location is out of the acceptable range."
        )

if __name__ == '__main__':
    unittest.main()
