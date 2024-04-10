from fleet.ambulance import Ambulance
from fleet.station import Station
from operations.incidentManager import  IncidentManager
from operations.incident_queue import  IncidentQueue
from operations.incident import Incident
from personnel import *
from datetime import datetime
from fleet.ambulanceQueue import AmbulanceQueue



def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance(1, "Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance3 = Ambulance(3, "Type C", "available", (50.090340, 19.920282), ["Defibrillator", "Oxygen tank"])
    ambulance4 = Ambulance(4, "Type B", "on mission", (50.045740, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance5 = Ambulance(5, "Type C", "available", (50.986340, 18.920282), ["Defibrillator", "Oxygen tank"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    queue = IncidentQueue()


    incident1 = Incident("Power outage in sector 4", "High", "2024-04-09 12:00", "John Doe", (50.095340, 18.528982))
    incident2 = Incident("Fire alarm in building 21", "Medium", "2024-04-09 12:30", "Jane Smith", (50.095340, 18.957286))
    incident3 = Incident("Fire alarm in building 15", "High", "2024-04-09 12:10", "John Duff", (50.185340, 18.528982))
    incident4 = Incident("Fire alarm in building 129", "Medium", "2024-04-09 11:30", "Jane Brown", (50.095340, 18.957886))
    queue += incident1
    queue += incident2
    queue += incident3
    queue += incident4

    # zadanie 4.
    # Utworzenie kolejki karetek
    ambulance_queue = AmbulanceQueue()
    ambulance_queue.push(ambulance1)
    ambulance_queue.push(ambulance2)
    ambulance_queue.push(ambulance3)
    ambulance_queue.push(ambulance4)
    ambulance_queue.push(ambulance5)

    incident_queue = IncidentQueue()
    incident_queue.push(incident1)
    incident_queue.push(incident2)
    incident_queue.push(incident3)
    incident_queue.push(incident4)

    
    incident_manager = IncidentManager(ambulance_queue, incident_queue)

    # Przypisanie karetek do incydentów
    incident_manager.assign_ambulance_to_incident()
    print(incident_queue)
    ##


    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    
    station = Station(station_id=1, location=(50.0, 19.0), ambulance=ambulance1, driver=driver1, additional_employee=employee1)

    # 3. Sprawdź, czy karetka jest na miejscu
    if station.is_ambulance_on_site():
        print("Karetka jest na miejscu.")
    else:
        print("Karetka nie jest na miejscu.")

if __name__ == "__main__":
    run_application()