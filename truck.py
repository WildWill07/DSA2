class Truck:
    def __init__(self, capacity, speed, packageLoad, mileage, address, departTime):
        self.capacity = capacity
        self.speed = speed
        self.packageLoad = packageLoad
        self.mileage = mileage
        self.address = address
        self.departTime = departTime

    def __str__(self):
        return "Truck Capacity: %s | Average Truck Speed: %smph | Packages on Truck: %s | Mileage: %s | Address: %s | Time of Departure: %s" % (self.capacity, self.speed, self.packageLoad, self.mileage, self.address, self.departTime)

    # Speed - 18 mph
    # capacity - 16
    # packageLoad
    # mileage
    # address
    # departTime - 8am earliest