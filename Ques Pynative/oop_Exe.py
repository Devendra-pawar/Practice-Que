#Exercise 1: Create a Class with instance attributes

# class Vehicle:
#     def __init__(self,max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# car = Vehicle(240,18)
# print(car.max_speed,car.mileage)

#Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#         pass

#Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self,name ,max_speed , mileage):
            self.name =name
            self.max_speed = max_speed
            self.mileage = mileage

class Bus(Vehicle):
     pass

School_bus = Bus("School Volvo",180,18)
print(School_bus.name,School_bus.max_speed,School_bus.mileage)
