import csv
from DS.HashMap import HashMap

class PackageDataReader:
    def __init__(self):
        self.csvFile = open('PackageData.csv') # For future generalization pass a variable to open method instead of an absolute definition
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

class DistanceDataReader:
    def __init__(self):
        pass