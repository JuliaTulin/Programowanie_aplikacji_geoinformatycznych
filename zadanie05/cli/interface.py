from fleet import *
from operations import *
from personnel import *
from logs import Logger
import datetime

class CLI:
    def __init__(self):
        self.ambulance_queue=AmbulanceQueue()
        self.ambulance_num=0

        self.employee_list=[]
        self.employee_num=0
        self.driver_num=0
        
        self.stations_list=[]
        self.station_num=0
        self.incident_queue = IncidentQueue()
    
    def check_resources(self):
        self.ambulance=int(input("Jaka jest ilosc dostepnych karetek?\n "))
        self.employee=int(input("Jaka jest ilosc dostepnego personelu?\n "))

        if self.employee >= 2*self.ambulance:
            Logger.info(f"{self.employee} to wystarczająaca liczba pracownikow aby obsłużyć {self.ambulance} karetki.")
            return True
        else:
            Logger.warn(f"{self.employee} to niewystarczajaca liczba pracownikow aby obsłużyć {self.ambulance} karetki.")
            return False

    def update_resources(self):
        self.ambulance_num=0
        for a in self.ambulance_queue:
            self.ambulance_num+=1
 
        self.employee_num=0
        self.driver_num=0
        for e in self.employee_list:
            if isinstance(e, Driver):
                self.driver_num+=1
            elif isinstance(e, Employee):
                self.employee_num+=1
        self.station_num=0
        for s in self.stations_list:
            self.station_num+=1

    def enough_station_resources(self):
        self.update_resources()
        if self.station_num <= self.employee_num:
            Logger.info("Wystarczająca liczba pracownikow")
        else:
            Logger.warn("Niewystarczajaca liczba pracownikow")
            
        if self.station_num <= self.driver_num:
            Logger.info("Wystarczająca liczba kierowcow")
        else:
            Logger.warn("Niewystarczajaca liczba kierowcow")

        if self.station_num <= self.ambulance_num:
            Logger.info("Wystarczająca liczba karetek")
        else:
            Logger.warn("Niewystarczajaca liczba karetek")

    def create_employee(self):
        try:
            print("\n--- TWORZENIE PRACOWNIKA ---\n")
            first_name = input("Imie:\n ")
            last_name = input("Nazwisko:\n ")
            ID = int(input("ID:\n "))
            salary = float(input("Wynagrodzenie:\n "))
            self.employee_list.append(Employee(first_name, last_name, ID, salary))
            self.employee_num+=1
            Logger.info("Created employee, " + str(self.employee_list[-1]))
        except:
            Logger.error("Problem with creating employee")


    def create_driver(self):
        try:
            print("\n--- TWORZENIE KIEROWCY ---\n")
            first_name = input("Imie:\n ")
            last_name = input("Nazwisko:\n ")
            ID = int(input("ID:\n "))
            salary = float(input("Wynagrodzenie:\n "))
            license_number = input("Numer rejestracyjny:\n ")
            print("Liczba kwalifikacji:")
            qualifications=[]
            for _ in range(int(input())):
                qualifications.append(input())
            self.employee_list.append(Driver(first_name, last_name, ID, salary, license_number, qualifications))
            self.driver_num+=1
            Logger.info("Created driver, " + str(self.employee_list[-1]))
        except:
            Logger.error("Problem with creating driver")

    def create_ambulance(self):
        try:
            print("\n--- TWORZENIE KARETKI ---")
            ID = int(input("ID:\n "))
            vehicle_type = input("Typ samochodu:")
            status = input("Status:\n ")
            x = float(input("Szerokość geograficzna:\n "))
            y = float(input("Długość geograficzna:\n "))
            print("Liczba sprzetow medycznych:")
            medical_equipment=[]
            for _ in range(int(input())):
                medical_equipment.append(input())
            self.ambulance_queue.push(Ambulance(ID, vehicle_type, status, (x,y), medical_equipment))
            self.ambulance_num+=1
            Logger.info("Created ambulance, " + str(self.ambulance_queue[-1]))
        except:
            Logger.error("Problem with creating ambulance")

    def create_station(self):
        try:
            print("\n--- TWORZENIE STACJI ---")
            station_id = int(input("ID:\n "))
            x = float(input("Szerokość geograficzna:\n "))
            y = float(input("Długość geograficzna:\n "))
            ambulance_id = int(input("ID karetki:\n "))
            ambulance = None
            for a in self.ambulance_queue:
                if a.id == ambulance_id:
                    ambulance = a
                    break
            driver_id = int(input("ID kierowcy:\n "))
            driver = None
            for d in self.employee_list:
                if isinstance(d, Driver) and d.employee_id == driver_id:
                    driver = d
                    break
            employee_id = int(input("ID pracownika:\n "))
            employee = None
            for e in self.employee_list:
                if not isinstance(e, Employee) and e.employee_id == employee_id:
                    employee = e
                    break
            self.stations_list.append(Station(station_id, (x,y), ambulance, driver, employee))
            Logger.info("Created station, " + str(self.stations_list[-1]))
        except:
            Logger.error("Problem with creating station")

    def create_incident(self):
        try:
            print("\n--- TWORZENIE ZDARZENIA ---")
            description = input("Opis:\n ")
            priority = input("Priorytet:\n ")
            # print("Czas zgloszenia:")
            now = datetime.datetime.now()
            reported_time = now.strftime('%Y-%m-%d %H:%M')
            reporter_info = input("Dane zglaszajacego:\n ")
            x = float(input("Szerokość geograficzna:\n "))
            y = float(input("Długość geograficzna:\n "))
            self.incident_queue.push(Incident(description, priority, reported_time, reporter_info, (x,y)))
            #self.ambulance_num+=1
            Logger.info("Created incident, " + str(self.incident_queue[-1]))
        except:
            Logger.error("Problem with creating incident")