class vehicle: 
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return f'number: {self.number}, color: {self.color}'

class manager:
    def __init__(self):
        self.vehicles  = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def change_vehicle(self, index, new_number = None, new_color = None):
        if new_number is not None:
            self.vehicles[index].number = new_number
        if new_color is not None:
            self.vehicles[index].color = new_color

    def show_vehicles(self):
        for i, vehicle in enumerate(self.vehicles):
            print(f'{i}: {vehicle}')

car1 = vehicle(3284,'silver')
car2 = vehicle(1122, 'Black')
car3 = vehicle(2315, 'red')

vehicle_manager = manager()

vehicle_manager.add_vehicle(car1)
vehicle_manager.add_vehicle(car2)
vehicle_manager.add_vehicle(car3)

vehicle_manager.show_vehicles()