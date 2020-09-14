# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass
#    def __init__(self, name):
#        self.name = name
#
class FlightVehicle(Vehicle):
    pass
#    def __init__(self, name, flight):
#        super().__init__(name)
#        self.flight = flight

class Starship(FlightVehicle):
    pass
#    def __init__(self, name, flight, crew):
#        super().__init__(name, flight)
#        self.crew = crew

class Airplane(FlightVehicle):
    pass
#    def __init__(self, name, flight, owner):
#        super().__init__(name, flight)
#        self.owner = owner


class GroundVehicle(Vehicle):
    pass
#    def __init__(self, name, dealer):
#        super().__init__(name)
#        self.dealer = dealer

class Car(GroundVehicle):
    pass
#    def __init__(self, name, dealer, make):
#        super().__init__(name, dealer)
#        self.make = make

class Motorcycle(GroundVehicle):
    pass
 #   def __init__(self, name, dealer, color):
 #       super().__init__(name, dealer)
 #       self.color = color



