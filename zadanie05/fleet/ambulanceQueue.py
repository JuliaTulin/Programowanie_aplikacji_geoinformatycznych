from .ambulance import *

class AmbulanceQueue:
    def __init__(self):
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]
    
    def push(self, item):
        self.__queue.append(item)

    def __setitem__(self, position, value):
        self.__queue[position] = value


    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


    def __iadd__(self, other):
        if isinstance(other, Ambulance):
            self.__queue.append(other)
        return self

    def pop(self, index=0):
        return self.__queue.pop(index)