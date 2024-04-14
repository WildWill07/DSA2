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
        #newMap = HashMap()
        for lines in self.csvReader:
            testMap.add(key=lines[0], data=lines)

    def close(self):
        self.csvFile.close() # Closes reader object after data has been loaded into the Hash Map

# Remove the below Code once main driver file is implemented
test = PackageDataReader()
testMap = HashMap()

test.loadHashMap()
test.close()
testMap.print()