from fleet.ambulanceQueue import AmbulanceQueue
from operations.incident import Incident
from datetime import datetime
import math

class IncidentManager:
    def __init__(self, ambulance_queue, incident_queue):
        self.ambulance_queue = ambulance_queue
        self.incident_queue = incident_queue

    def distance(self, lat1, lon1, lat2, lon2): # sposób na obliczenie odległości między punktami na Ziemi
        R = 6371.0  
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    def assign_ambulance_to_incident(self):
        if self.ambulance_queue and self.incident_queue:
            for incident in self.incident_queue:
                min_distance =  float('inf')
                closest_ambulance = None
                for ambulance in self.ambulance_queue:
                    if ambulance.status == "available":
                        distance = self.distance(incident.incident_location[0], incident.incident_location[1], ambulance.location[0], ambulance.location[1])
                        if distance < min_distance:
                            min_distance = distance
                            closest_ambulance = ambulance
                if closest_ambulance:
                    closest_ambulance.update_status("on mission")
                    print(f"Ambulance {closest_ambulance.id}, {closest_ambulance.medical_equipment} assigned to incident: {incident.description}")
                else:
                    print(f"No available ambulance for incident: {incident.description}")
        else:
            print("No available ambulances or incidents.")
