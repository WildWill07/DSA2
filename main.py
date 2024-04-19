from DS.HashMap import HashMap
from truck import Truck
import csv
import datetime

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

def getMinDistance():
    return

truck1 = Truck(16, 18, [1, 2, 4, 5, 7, 8, 10, 13, 14, 15, 16, 19], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck(16, 18, [31, 33, 34, 35, 37, 39, 40, 3, 9, 18, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = Truck(16, 18, [11, 12, 17, 20, 21, 22, 23, 24, 26, 27, 29, 30, 6, 25, 28, 32], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

def main():
    packageHashMap = HashMap()

    packageHashMap.loadHashMap(csvPackage)
    
    print(truck1)
    print(truck2)
    print(truck3)

if __name__ == "__main__":
    main()