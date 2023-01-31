class ParkingLot:
    def __init__(self, max_spaces):
        self.max_spaces = max_spaces
        self.occupied_spaces = 0
        self.parked_vehicles = {}

    def park_vehicle(self, vehicle_id):
        if self.occupied_spaces < self.max_spaces:
            self.occupied_spaces += 1
            self.parked_vehicles[vehicle_id] = True
            print(f"Vehicle {vehicle_id} parked successfully.")
        else:
            print("Parking lot is full.")

    def leave_vehicle(self, vehicle_id):
        if vehicle_id in self.parked_vehicles:
            del self.parked_vehicles[vehicle_id]
            self.occupied_spaces -= 1
            print(f"Vehicle {vehicle_id} left the parking lot.")
        else:
            print(f"Vehicle {vehicle_id} not found in the parking lot.")

parking_lot = ParkingLot(5)
parking_lot.park_vehicle("a")
parking_lot.park_vehicle("b")
parking_lot.leave_vehicle("a")
parking_lot.park_vehicle("c")
parking_lot.park_vehicle("d")
parking_lot.park_vehicle("e")
parking_lot.park_vehicle("f")
parking_lot.park_vehicle("g")
parking_lot.leave_vehicle("i")