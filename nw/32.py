class vehicle:
    def engine(self):
        print("The engine is starting")
class car(vehicle):
    def drive(self):
        print("Thecar is driving")
obj=car()
obj.engine() 
obj.drive()