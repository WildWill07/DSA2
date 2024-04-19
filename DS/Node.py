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

    def __str__(self):
        return "Package ID: %s | Package Address: %s, %s, UT, %s | Package Weight: %skg | Delivery Deadline: %s | Package Status: %s | Time of Delivery: %s" % (self.PackageID, self.D_Address, self.D_City, self.D_ZipCode, self.Weight, self.D_Deadline, self.D_Status, self.deliveryTime)