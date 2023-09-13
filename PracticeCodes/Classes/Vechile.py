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

    """
    Comment1:- Formate the file. There are lot of highlighting underlines showing in the code.
    
    Comment2: - The name of the arguments in  the constructor class are not in the camel format.
    
    Comment3: - The name of the function names are not in the camel format.
    
    comment4: - Name of the object in the line 14 is not in the cammel format.
    
    """

