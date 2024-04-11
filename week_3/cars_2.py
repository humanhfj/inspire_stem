
class car:
    def _init_(self,model,make,year_of_production,fuel_capacity,horse_power):
        self.model = model
        self.make = make
        self.year_of_productin =year_of_production
        self.fuel_capacity = fuel_capacity
        self.fuel = horse_power


    def print_make(self,make):
        print("The car is of {0} make".format(self.make))


my_car =car("Subaru","Impreza","2013","3500cc","black",)
friends_car =car("Supra","Nissan","2013","3500cc","black",)

my_car.set_make("Ford")
friends_car.set_make("Toyota")


def set_make_(self,make):
    self,make=make

def get_make(self):
    return self.make


   