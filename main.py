from DS.HashMap import HashMap
from csvReader import *
from truck import Truck
import csv

with open("CSV/PackageData.csv") as file:
    csvPackage = csv.reader(file)
    csvPackage = list(csvPackage)

with open("CSV/DistanceTable.csv") as file:
    csvDistance = csv.reader(file)
    csvDistance = list(csvDistance)

with open("CSV/AddressTable.csv") as file:
    csvAddress = csv.reader(file)
    csvAddress = list(csvAddress)


def main():
    packageHashMap = HashMap()
    startAddress = "4001 South 700 East" # Hub Address

    packageHashMap.loadHashMap(csvPackage)
    packageHashMap.print()
    #findMinDistance(addressReader ,startAddress)
    

def getDistance(address1, address2):
    # Find index for each address in the addressReader list
    # Use returned indexes to access value in distanceReader 2D array
    # If element accessed == '' flip column & row indexes
    # return value
    pass

def findMinDistance(pAddressReader, pStartAddress):
    # Begin at current address
    # Find address index in addressTable.csv
    addressReader = pAddressReader
    currentAddress = pStartAddress 
    idx = addressReader.getIndex(currentAddress)
    print(idx)
    
    pass

def getAddressIndex(address):
    pass


if __name__ == "__main__":
    main()


# Define Starting Address
# Get Starting Address Index
# Iterate through distanceReader values associated with starting address index
# Store shortest distance
# Locate Address index of the shortest distance