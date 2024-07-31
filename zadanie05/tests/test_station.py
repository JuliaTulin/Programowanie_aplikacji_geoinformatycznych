import unittest
from unittest.mock import MagicMock
from datetime import datetime
from fleet import *
from personnel import Driver
from operations import Incident

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestStation(unittest.TestCase):

    def setUp(self):
        self.mock_ambulance = MagicMock(spec=Ambulance)
        self.mock_driver = MagicMock(spec=Driver)
        self.mock_additional_employee = MagicMock()
        
        self.station_location = (50.0, 19.0)
        self.ambulance_location = (50.0, 19.0)
        
        self.mock_ambulance.location = self.ambulance_location
    
        self.station = Station(
            station_id=1,
            location=self.station_location,
            ambulance=self.mock_ambulance,
            driver=self.mock_driver,
            additional_employee=self.mock_additional_employee
        )

    def test_init(self):
        self.assertEqual(self.station.station_id, 1)
        self.assertEqual(self.station.location, self.station_location)
        self.assertEqual(self.station.ambulance, self.mock_ambulance)
        self.assertEqual(self.station.driver, self.mock_driver)
        self.assertEqual(self.station.additional_employee, self.mock_additional_employee)

    def test_is_ambulance_on_site(self):
        self.assertTrue(self.station.is_ambulance_on_site())
        self.mock_ambulance.location = (51.0, 20.0)
      
