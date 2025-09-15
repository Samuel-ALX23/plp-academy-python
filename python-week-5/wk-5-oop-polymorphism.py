# This program demonstrates polymorphism using a base Vehicle class
# and several specialized vehicle classes.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"The {self.brand} is moving...")

class Car(Vehicle):
    def move(self):
        print(f"The {self.brand} is **driving** 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.brand} is **flying** ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"The {self.brand} is **sailing** ⛵")


if __name__ == "__main__":
    # Create instances (objects) of each of the vehicle classes.
    my_car = Car("Ford")
    my_plane = Plane("Boeing")
    my_boat = Boat("Jeanneau")

    # Now, let's put all the objects into a single list.
    vehicles = [my_car, my_plane, my_boat]

    print("Demonstrating Polymorphism:")
    print("Each vehicle is being told to 'move()', but they do it differently.\n")

    # We loop through the list and call the SAME `move()` method on each object.
    for vehicle in vehicles:
        vehicle.move()

    print("\n")
    print("--------------------------------------------------")
    print("The program successfully demonstrated polymorphism.")
    print("Notice how the same `.move()` call resulted in different actions.")
