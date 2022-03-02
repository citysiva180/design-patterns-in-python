# Example code to observe cohesion and coupling
import string
import random


# created 2 classes specfic to info and final instance
class VehicleInfo:

    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    brand: str
    catalogue_price: int
    electric: bool

    def compute_tax(self):
        tax_percentage = 0.02 if self.electric else 0.05
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand : {self.brand}")
        print(f"Payable Tax : {self.compute_tax()}")


class Vehicle:

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    id: str
    license_plate: str
    info: VehicleInfo

    def print(self):
        print(f"ID : {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagon ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(
            brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):

        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)


app = Application()
Tesla = app.register_vehicle("Tesla Model 3")
Tesla.print()
print()
BMW_5 = app.register_vehicle("BMW 5")
BMW_5.print()
