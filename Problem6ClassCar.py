# Kadari Faulkner
# 12/12/2021
# problem 6 the python class

class car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def the_type(self):
        return self.type

    def the_model(self):
        return self.model

    def the_year(self):
        return self.year

    def the_color(self):
        return self.color

    def the_manufacturer(self):
        return self.manufacturer

    def full_specs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type

car1 = car("Sports", 2012, "Blue", "Limited", "Mustang")
car2 = car("Sedan", 2020, "Black", "Limited", "Mustang")

print(car1.the_color())
print(car1.the_model())
print(car2.the_color())
print(car2.the_model())
print(car1.full_specs())
print(car2.full_specs())
