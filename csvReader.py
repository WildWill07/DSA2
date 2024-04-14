import csv
from DS.HashMap import HashMap

class PackageDataReader:
    def __init__(self):
        self.csvFile = open('PackageData.csv')
        self.csvReader = csv.reader(self.csvFile)

    def print(self):
        for lines in self.csvReader:
            print(lines[0])

    def loadHashMap(self):
        next(self.csvReader, None) # Skips header row of csv Data
        newMap = HashMap()
        for lines in self.csvReader:
            newMap.add(key=lines[0], data=lines)

    def close(self):
        self.csvFile.close() # Closes reader object after data has been loaded into the Hash Map


test = PackageDataReader()

test.loadHashMap()
test.close()

# data parameter is a tuple containing the following:
# PackageID - int 0
# D_Address - str 1
# D_City - str 2
# D_ZipCode - int 3
# D_Deadline - str 4
# Weight - int 5
# D_Status - str 6