class PackageNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

        self.PackageID = data[0]
        self.D_Address = data[1]
        self.D_City = data[2]
        self.D_ZipCode = data[3]
        self.D_Deadline = data[4]
        self.Weight = data[5]
        self.D_Status = data[6]
        self.deliveryTime = None
        self.departTime = None
        self.truckID = None

    def __str__(self):
        return "ID: %s | Weight: %skg | Deadline: %s | Status: %s | Truck ID: %s | Scheduled Departure Time: %s | Scheduled Delivery: %s | Address: %s, %s, UT, %s" % (self.PackageID, self.Weight, self.D_Deadline, self.D_Status, self.truckID, self.departTime, self.deliveryTime, self.D_Address, self.D_City, self.D_ZipCode)
    
    def verifyStatus(self, time):
        if time > self.deliveryTime:
            self.D_Status = "DELIVERED"
        elif time < self.departTime:
            self.D_Status = "HUB"
        else:
            self.D_Status = "EN-ROUTE"