from .incident import Incident

class IncidentQueue:
    def __init__(self):
        self.__queue = []

    def push(self, item):
        self.__queue.append(item)

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def assign_ambulance(self, incident_id, ambulance):
        for incident in self.__queue:
            if incident.id == incident_id:
                incident.assigned_ambulance = ambulance

    def __str__(self):
        result = "Incident Queue:\n"
        for incident in self.__queue:
            result += f"Incident ID: {incident.id}, Description: {incident.description}\n"
            if hasattr(incident, 'assigned_ambulance'):
                result += f"Assigned Ambulance: {incident.assigned_ambulance}\n"
        return result

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:] 
            new__queue += other
            return new__queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)

if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident(1, "Power outage in sector 4", "High", "2024-04-09 12:00", "John Doe", (50.095340, 18.528982))
    incident2 = Incident(2, "Fire alarm in building 21", "Medium", "2024-04-09 12:30", "Jane Smith", (50.005340, 18.957286))
    incident3 = Incident(3, "Fire alarm in building 15", "High", "2024-04-09 12:10", "John Duff", (50.185340, 18.528982))
    incident4 = Incident(4, "Fire alarm in building 129", "Medium", "2024-04-09 11:30", "Jane Brown", (50.095340, 18.957886))

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    print(queue)
    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident4
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])
    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
    new_incident = Incident(3, "Test incident")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))