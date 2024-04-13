import csv

class PackageDataReader:
    def __init__(self):
        self.csvFile = open('PackageData.csv')
        self.csvReader = csv.reader(self.csvFile)

    def print(self):
        for lines in self.csvReader:
            print(lines)

    def close(self):
        self.csvFile.close()


test = PackageDataReader()
test.print()
test.close()