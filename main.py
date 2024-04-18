from DS.HashMap import HashMap
from truck import Truck
import csv

# imports necessary csv data and saves data in a list 2D list object
with open("CSV/PackageData.csv") as file:
    csvPackage = csv.reader(file)
    csvPackage = list(csvPackage)

with open("CSV/DistanceTable.csv") as file:
    csvDistance = csv.reader(file)
    csvDistance = list(csvDistance)

with open("CSV/AddressTable.csv") as file:
    csvAddress = csv.reader(file)
    csvAddress = list(csvAddress)

# Searches csvAddress data for a matching address and then returns corresponding address index
def getAddressIndex(address):
    for x in range(len(csvAddress)):
        if csvAddress[x][2] == address:
            return int(csvAddress[x][0])
        
# Takes two address indexes and returns the distance between the two nodes listed in the csvDistance Adj Matrix (2D list)
# If value is empty then swap axis
def getDistance(add1, add2):
    distance = csvDistance[add1][add2]
    if csvDistance[add1][add2] == '':
        distance = csvDistance[add2][add1]
    return float(distance)

def main():
    packageHashMap = HashMap()
    startAddress = "4001 South 700 East" # Hub Address
    someAddress = "4300 S 1300 E"

    packageHashMap.loadHashMap(csvPackage)
    print(getDistance(getAddressIndex(startAddress), getAddressIndex(someAddress)))

if __name__ == "__main__":
    main()


# Define Starting Address
# Get Starting Address Index
# Iterate through distanceReader values associated with starting address index
# Store shortest distance
# Locate Address index of the shortest distance