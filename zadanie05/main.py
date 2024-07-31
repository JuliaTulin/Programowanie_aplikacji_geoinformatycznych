from fleet import *
from operations import *
from personnel import *
from datetime import datetime
from logs import *
from cli import *


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance(1, "Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance3 = Ambulance(3, "Type C", "available", (50.090340, 19.920282), ["Defibrillator", "Oxygen tank"])
    ambulance4 = Ambulance(4, "Type B", "on mission", (50.045740, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance5 = Ambulance(5, "Type C", "available", (50.986340, 18.920282), ["Defibrillator", "Oxygen tank"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)
    app.employee_list.append(employee1)
    app.employee_list.append(employee2)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])
    app.employee_list.append(driver1)
    app.employee_list.append(driver2)

    # sprawdzenie nie są te same karetki
    if ambulance1 == ambulance2:
        Logger.error("To sa te same karetki!")
    # sprawdzenie ile mamy karetek
    Logger.info(Ambulance.get_instances_count())



    incident1 = Incident("Power outage in sector 4", "High", "2024-04-09 12:00", "John Doe", (50.095340, 18.528982))
    incident2 = Incident("Fire alarm in building 21", "Medium", "2024-04-09 12:30", "Jane Smith", (50.095340, 18.957286))
    incident3 = Incident("Fire alarm in building 15", "High", "2024-04-09 12:10", "John Duff", (50.185340, 18.528982))
    incident4 = Incident("Fire alarm in building 129", "Medium", "2024-04-09 11:30", "Jane Brown", (50.095340, 18.957886))


    # zadanie 4.
    # Utworzenie kolejki karetek
    # ambulance_queue = AmbulanceQueue()
    app.ambulance_queue.push(ambulance1)
    app.ambulance_queue.push(ambulance2)
    app.ambulance_queue.push(ambulance3)
    app.ambulance_queue.push(ambulance4)
    app.ambulance_queue.push(ambulance5)

    # incident_queue = IncidentQueue()
    app.incident_queue.push(incident1)
    app.incident_queue.push(incident2)
    app.incident_queue.push(incident3)
    app.incident_queue.push(incident4)

    
    incident_manager = IncidentManager(app.ambulance_queue, app.incident_queue)

    # Przypisanie karetek do incydentów
    incident_manager.assign_ambulance_to_incident()
    Logger.debug(app.incident_queue)
    ##


    # daj kierowcy podwyżkę za super zasługi
    Logger.info(f"Przed podwyzka: {driver1}")
    driver1.update_salary(5000.12)
    Logger.info(f"Po podwyzce: {driver1}")

    
    station = Station(station_id=1, location=(50.0, 19.0), ambulance=ambulance1, driver=driver1, additional_employee=employee1)
    app.stations_list.append(station
    )
    # 3. Sprawdź, czy karetka jest na miejscu
    if station.is_ambulance_on_site():
        Logger.info("Karetka jest na miejscu.")
    else:
        Logger.warn("Karetka nie jest na miejscu.")


# interakcja programu z użytkownikiem
def display_menu():
    print("\nCo chcesz zrobić?")
    print("a) Dodaj pracownika")
    print("b) Dodaj kierowcę")
    print("c) Dodaj karetkę")
    print("d) Dodaj incydent")
    print("e) Dodaj stację")
    print("f) Sprawdź zasoby")
    print("g) Sprawdź, czy stacja ma wystarczające zasoby")
    print("h) Wyjście")
    return input("Wybierz opcję: ").strip().lower()


if __name__ == "__main__":
    app = CLI()
    run_application()
    while True:
        choice = display_menu()
        if choice == 'a':
            app.create_employee()
        elif choice == 'b':
            app.create_driver()
        elif choice == 'c':
            app.create_ambulance()
        elif choice == 'd':
            app.create_incident()
        elif choice == 'e':
            app.create_station()
        elif choice == 'f':
            app.check_resources()
        elif choice == 'g':
            app.enough_station_resources()
        elif choice == 'h':
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")