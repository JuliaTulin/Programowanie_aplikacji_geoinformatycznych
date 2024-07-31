import unittest
from logs import Logger
from fleet import Ambulance
from unittest.mock import MagicMock

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestAmbulance(unittest.TestCase):

    def setUp(self):
        # Przygotowanie danych testowych
        Ambulance._Ambulance__max_id = 0
        self.ambulance = Ambulance(
            id=0,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator", "stretcher"]
        )

    def test_initialization(self):
        self.assertEqual(self.ambulance.vehicle_type, "AZ124")
        self.assertEqual(self.ambulance.status, "available")
        self.assertEqual(self.ambulance.location, (50.095340, 19.920282))
        self.assertListEqual(self.ambulance.medical_equipment, ["defibrillator", "stretcher"])

    def test_update_location(self):
        new_location = (51.095340, 20.920282)
        self.ambulance.update_location(new_location)
        self.assertEqual(self.ambulance.location, new_location)

    def test_update_status(self):
        new_status = "on_mission"
        self.ambulance.update_status(new_status)
        self.assertEqual(self.ambulance.status, new_status)

    def test_valid_location(self):
        valid_location = (50.095340, 19.920282)
        invalid_location = (61.0, -190.0)  # Poza zakresem
        self.assertTrue(self.ambulance._valid_location(valid_location))
        self.assertFalse(self.ambulance._valid_location(invalid_location))

    def test_eq(self):
        another_ambulance = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator", "stretcher"]
        )
        self.assertNotEqual(self.ambulance, another_ambulance)

    def test_validate_id(self):
        self.assertTrue(Ambulance.validate_id(123))
        self.assertFalse(Ambulance.validate_id("123"))

    def test_get_instances_count(self):
        count = Ambulance.get_instances_count()
        self.assertEqual(count, "Number of working ambulances: 1")

    def test_invalid_location_error(self):
        Logger.error = MagicMock()
        Ambulance(id=2, vehicle_type="AZ125", status="available", location=(91.0, 190.0), medical_equipment=[])
        Logger.error.assert_called_once_with("Ambulance 2 ((91.0, 190.0)) - Location is out of the acceptable range.")

if __name__ == '__main__':
    unittest.main()
