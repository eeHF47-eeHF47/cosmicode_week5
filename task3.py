# Create a program to demonstrate the concept of inheritance by creating a base class for a vehicle and derived classes for car and bike.
class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
# method engine
    def start_engine(self):
        print(f"The {self.color} {self.make} {self.model} engine has started.")

    def stop_engine(self):
        print(f"The {self.color} {self.make} {self.model} engine has stopped.")

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model} in {self.color}.")
#  derived class

class Car(Vehicle):
    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year, color)
        self.num_doors = num_doors

    def open_trunk(self):
        print(f"The trunk of the {self.color} {self.make} {self.model} is open.")

    def display_info(self):
        super().display_info()
        print(f"It is a car with {self.num_doors} doors.")

# derived class
class Bike(Vehicle):
    def __init__(self, make, model, year, color, type_of_bike):
        super().__init__(make, model, year, color)
        self.type_of_bike = type_of_bike

    def kick_start(self):
        print(f"The {self.color} {self.make} {self.model} has been kick-started.")

    def display_info(self):
        super().display_info()
        print(f"It is a {self.type_of_bike} bike.")


# Example usage:
car = Car("Toyota", "Camry", 2022, "blue", 4)
bike = Bike("Yamaha", "MT-07", 2021, "black", "sport")

car.start_engine()
car.open_trunk()
car.display_info()
car.stop_engine()

print("\n")

bike.start_engine()
bike.kick_start()
bike.display_info()
bike.stop_engine()
