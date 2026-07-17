class vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year 
    def info(self):
        print(f"{self.brand} , {self.year}")
    
class ElectricVehicle(vehicle):
    def __init__(self, capacity):
        self.capacity = capacity
    def charge(self):
        print(f"Battery: {self.capacity}kWh")

class car(vehicle):
    def __init__(self,model,brand, year):
        super().__init__(brand, year)
        self.model = model
    def drive(self):
        print(f"{self.brand} {self.model} is driving")
        
class ElectricCar(ElectricVehicle, car):
    def __init__(self, brand, year, model, capacity):
        car.__init__(self, model, brand, year)
        ElectricVehicle.__init__(self, capacity)
    def autopilot(self): 
        print(f"Autopilot ON in {self.brand} {self.model} {self.year}")

v1 = vehicle("BMW",2025)
v1.info()        

ev1 = ElectricVehicle(12000)
ev1.charge()

ev2 = car("M5","BMW",2025)
ev2.drive()

ev3 = ElectricCar("BMW", 2026, "M5", 12000)
ev3.autopilot()
