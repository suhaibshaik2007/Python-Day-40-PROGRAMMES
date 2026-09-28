# VEHICLE - START AND STOP

from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("CAr Stopped")

class Bike(Vehicle):
    def start(self):
            print("Bike Started")
    
    def stop(self):
            print("Bike Stopped")

c = Car()
b = Bike()

c.start()
c.stop()
b.start()
b.stop ()