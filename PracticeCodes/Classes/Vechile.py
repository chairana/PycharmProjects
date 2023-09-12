class Vehicle:
    def __init__(self,vehicleType, maxSpeed,milage):
        self.vehicleType= vehicleType
        self.maxSpeed=maxSpeed
        self.milage=milage

    def getvehicletype(self):
        print(self.vehicleType)

    def getmilage(self):
        print(self.milage)

if __name__ == "__main__":
    vehicleobj= Vehicle("car","50mph","25km")
    vehicleobj.getvehicletype()
    vehicleobj.getmilage()

    #Todo: - Create the class object variable for Vechile
    #Todo: - Print the vehileType, MaxSpeed and Milages using the object
