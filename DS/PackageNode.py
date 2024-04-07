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

# data parameter is a tuple containing the following:
# PackageID - int
# D_Address - str
# D_City - str
# D_ZipCode - int
# D_Deadline - str
# Weight - int
# D_Status - str