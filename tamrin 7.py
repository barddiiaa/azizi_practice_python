class Vehicle:
    def init(self, wheels, year, power):
        self.wheels = wheels
        self.year = year
        self.power = power

    def str(self):
        return f"Vehicle with {self.wheels} wheels, year {self.year}, power {self.power} HP"

class Car(Vehicle):
    def init(self, wheels, year, power, model, name, price):
        super().init(wheels, year, power)
        self.model = model
        self.name = name
        self.price = price

    def str(self):
        return f"Car: {self.name} {self.model}, {self.year}, {self.power} HP, {self.wheels} wheels, ${self.price}"

class Truck(Vehicle):
    def init(self, wheels, year, power, model, name, price):
        super().init(wheels, year, power)
        self.model = model
        self.name = name
        self.price = price

    def str(self):
        return f"Truck: {self.name} {self.model}, {self.year}, {self.power} HP, {self.wheels} wheels, ${self.price}"

class Motorcycle(Vehicle):
    def init(self, wheels, year, power, model, name, price):
        super().init(wheels, year, power)
        self.model = model
        self.name = name
        self.price = price

    def str(self):
        return f"Motorcycle: {self.name} {self.model}, {self.year}, {self.power} HP, {self.wheels} wheels, ${self.price}"

# نمونه استفاده از کلاس‌ها

car = Car(4, 2022, 200, "Sedan", "Toyota Camry", 30000)
truck = Truck(6, 2021, 400, "Heavy Duty", "Ford F-150", 50000)
motorcycle = Motorcycle(2, 2023, 150, "Sport", "Yamaha R1", 20000)

print(car)
print(truck)
print(motorcycle)
