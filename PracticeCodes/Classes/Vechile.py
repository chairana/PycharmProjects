class Vehicle:
    def __init__(self, vehicleType, maxSpeed, milage):
        self.vehicleType = vehicleType
        self.maxSpeed = maxSpeed
        self.milage = milage

    def getVehicleType(self):
        print(self.vehicleType)

    def getMaxSpeed(self):
        print(self.maxSpeed)

    def getMilage(self):
        print(self.milage)


if __name__ == "__main__":
    vehicleObj = Vehicle("car", "50mph", "25km")
    vehicleObj.getVehicleType()
    vehicleObj.getMilage()
    vehicleObj.getMaxSpeed()

#<<<<<<< Updated upstream
    """
    Comment1:- Formate the file. There are lot of highlighting underlines showing in the code.
    
    Comment2: - The name of the arguments in  the constructor class are not in the camel format.
    
    Comment3: - The name of the function names are not in the camel format.
    
    comment4: - Name of the object in the line 14 is not in the camel format.
    
    """

    # Todo: - Create the class object variable for Vechile
    # Todo: - Print the vehileType, MaxSpeed and Milages using the object
#>>>>>>> Stashed changes
