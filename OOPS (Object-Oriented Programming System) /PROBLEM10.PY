class vehicles:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery
    @staticmethod
    def start():
        print("Vehicle started")

class car(vehicles):
    def __init__(self, brand,model,battery):
        super().__init__(brand,model,battery)
    @staticmethod
    def drive():
        print("Vehicle is driving")

class electric_car(car):
    def __init__(self, brand,model,battery):
        super().__init__(brand,model,battery)
    @staticmethod
    def charge():
        print("Vehicle is charging")

ec1 = electric_car("Tesla", "Model S", "100kWh")
ec1.start()
ec1.drive()
ec1.charge()
