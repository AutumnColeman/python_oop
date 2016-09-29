#Create a class Vehicle. A Vehicle object will have 3 attributes.
print "\n"
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print car.make, car.model, car.year

car = Vehicle("Nissan", "Leaf", "2015")
print car.make, car.model, car.year

#Add a print_info method to the Vehicle class.
car.print_info()
