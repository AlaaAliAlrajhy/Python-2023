# 1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. (__init__)


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#  usage
car = Vehicle(200, 50)
print(f"Max Speed: {car.max_speed} km")
print(f"Mileage: {car.mileage} km")

#%%
# 2. Give the Vehicle class a method seating_capacity() that will take capacity as an argument and return the string "The seating capacity of (name of the vehicle) is (capacity)."

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of this vehicle is {capacity}."

#  usage
car = Vehicle(200, 50)
print(car.seating_capacity(5))
print(f"Max Speed: {car.max_speed} km")
print(f"Mileage: {car.mileage} km")


# %%
# Write the method seating_capacity() again with capacity as its argument in the Bus class .....

class Vehicle:
    def __init__(self, max_speed, mileage):
        print("Vehicle has been created")
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of this vehicle is {capacity}."

# creat a child class
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


car = Vehicle(200, 50)
bus = Bus(120, 30)

print(car.max_speed, car.mileage)
print(bus.max_speed, bus.mileage)

print(car.seating_capacity(5))
print(bus.seating_capacity())  # Default capacity of 50

#%%
# Make sure that all the parts of the solution work 
class Vehicle:
    def __init__(self, max_speed, mileage):
        print("Vehicle has been created")
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of this vehicle is {capacity}."

# child class
class Bus(Vehicle):
    color = "white"

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


car = Vehicle(200, 50)
bus = Bus(120, 30)

print(car.max_speed, car.mileage)
print(bus.max_speed, bus.mileage)

print(car.seating_capacity(5))
print(bus.seating_capacity())

print(bus.color)
