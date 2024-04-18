import csv
from DS.HashMap import HashMap

# Reads data from Package PackageData.csv
class PackageDataReader:
    def __init__(self):
        self.csvFile = open('CSV\PackageData.csv') # For future generalization pass a variable to open method instead of an absolute definition
        self.csvReader = csv.reader(self.csvFile)

    def print(self):
        for lines in self.csvReader:
            print(lines[0])

    def loadHashMap(self, map):
        next(self.csvReader, None) # Skips header row of csv Data
        newMap = map # assigns imported hash map object
        for lines in self.csvReader:
            newMap.add(key=lines[0], data=lines)

    def close(self):
        self.csvFile.close() # Closes reader object after data has been loaded into the Hash Map

# Reads data from DistanceTable.csv
class DistanceDataReader:
    def __init__(self):
        self.csvFile = open('CSV\DistanceTable.csv')
        self.csvDistance = list(csv.reader(self.csvFile)) # Converts input into a list/arr obj

    def close(self):
        self.csvFile.close()

    # Prints data stored in csvDistance by row
    def print(self):
        for x in range(len(self.csvDistance)):
            print(self.csvDistance[x])

    # Converts csvDistance data entries to float type
    def typeConversion(self):
        temp = []
        for row in self.csvDistance:
            test = []
            for item in row:
                test.append(float(item))
            temp.append(test)
        self.csvDistance = temp