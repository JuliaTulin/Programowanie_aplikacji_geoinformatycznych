from logs import Logger

class Incident:
    __max_id = 0

    def __init__(self, description, priority, reported_time, reporter_info, incident_location):
        
        if not self._valid_location(incident_location):
            Logger.error(f"Incident {description} ({incident_location}) - Location is out of the acceptable range.")
        
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        # zadanie 3
        self.priority = priority
        self.reported_time = reported_time
        self.reporter_info = reporter_info
        self.incident_location = incident_location

    def __str__(self):
        return f"\nIncident ID: {self.id}, \nDescription: {self.description}, \nPriority: {self.priority}, \nReported Time: {self.reported_time}, \nReporter: {self.reporter_info} \nLocalization: {self.incident_location}"

    def __eq__(self, other):
        if not isinstance(other, Incident):
            return NotImplemented
        return self.id == other.id

    def __repr__(self):
        return f"\nIncident({self.description}, {self.priority}, {self.reported_time}, {self.incident_lacation!r})"

    def _valid_location(self, location):
        northing, easting = location
        return (-90.0 <= northing <= 90.0 and
                -180.0 <= easting <= 180.0)