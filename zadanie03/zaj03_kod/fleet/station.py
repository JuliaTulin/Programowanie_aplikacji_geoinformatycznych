import fleet as F
import operations as OP
import personnel as P

class Station:
    def __init__(self, station_id, location, ambulance, driver, additional_employee):
        self.station_id = station_id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.additional_employee = additional_employee

    def is_ambulance_on_site(self):
        """
        Sprawdzenie, czy karetka jest na miejscu.
        """
        return self.location == self.ambulance.location

    def __str__(self):
        return f"Station ID: {self.station_id}\nLocation: {self.location}\nAmbulance: {self.ambulance}\nDriver: {self.driver}\nAdditional Employee: {self.additional_employee}"
    
    def assign_ambulances_to_incidents(self, incidents):
        pass
