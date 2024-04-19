class Truck:
    def __init__(self, capacity, speed, packageLoad, mileage, address, time):
        self.capacity = capacity
        self.speed = speed
        self.packageLoad = packageLoad
        self.mileage = mileage
        self.address = address
        self.time = time

    def __str__(self):
        return "Truck Capacity: %s | Average Truck Speed: %smph | Packages on Truck: %s | Mileage: %s | Address: %s | Delivery Completed at: %s" % (self.capacity, self.speed, self.packageLoad, self.mileage, self.address, self.time)

    # Speed - 18 mph
    # capacity - 16
    # packageLoad
    # mileage
    # address
    # departTime - 8am earliest