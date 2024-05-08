from DS.HashMap import HashMap
from truck import Truck
import csv
import datetime

# Student ID: 011476838
# Name: William Neyland

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

# Gets user input and converts it to a valid time
def timeConversion():
    inputTime = input("Please enter a valid time in the following format, HH:MM:SS (exemple '10:30:00'): ")
    try:
        (h, m, s) = inputTime.split(":")
        convertedTime = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # Manually Update package address for package 9 @ 10:20:00
        if convertedTime < datetime.timedelta(hours=10, minutes=20, seconds=0):
            package = packageHashMap.getNodeObject(9)
            package.D_Address = "300 State St"
            package.D_ZipCode = "84103"
        return convertedTime
    except ValueError:
        print("ERROR: Provided invalid input exiting the application now")
        exit()

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

# Implements Dijkstra's algorithm to determine MST of Nodes used to plan optimal package delivery route
# Takes in a truck object as the parameter
def deliver(truckX):
    temp = truckX.packageLoad.copy()
    for id in truckX.packageLoad:
        (packageHashMap.getNodeObject(id)).departTime = truckX.time
    truckX.packageLoad.clear()

    while(len(temp) > 0):
        minDistance = 10e8
        for id in temp:
            node = packageHashMap.getNodeObject(id)
            if (getDistance(getAddressIndex(truckX.address), getAddressIndex(node.D_Address)) < minDistance):
                minDistance = getDistance(getAddressIndex(truckX.address), getAddressIndex(node.D_Address))
                selectedNode = node # stores node obj mem addr of shortest distance node
        truckX.packageLoad.append(selectedNode.PackageID)
        temp.remove(selectedNode.PackageID)
        truckX.address = selectedNode.D_Address
        truckX.mileage += minDistance
        truckX.time += datetime.timedelta(hours=minDistance/18)
        selectedNode.deliveryTime = truckX.time
        selectedNode.D_Status = "DELIVERED" # Update status of package once delivered
    
# Initialize Truck Objects for delivery
truck1 = Truck(16, 18, [1, 2, 4, 5, 7, 8, 10, 13, 14, 15, 16, 19], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck(16, 18, [31, 33, 34, 35, 37, 39, 40, 3, 9, 18, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = Truck(16, 18, [11, 12, 17, 20, 21, 22, 23, 24, 26, 27, 29, 30, 6, 25, 28, 32], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

# Initialize and load Hash Map
packageHashMap = HashMap()
packageHashMap.loadHashMap(csvPackage)

# Driver Code
def main():
    deliver(truck1)
    deliver(truck2)
    deliver(truck3)

    print("========================================================================================================\n")
    print("Welcome to Package Router.")
    print("This program was written and developed by William Neyland\n")
    print("The total distance traveled by all delivery trucks is: " + str(truck1.mileage + truck2.mileage + truck3.mileage) + " miles")
    print("To check the status of specific package please enter 'sp' or to check the status of all packages enter 'all'.")
    try:
        userInput = input()
        if userInput == 'sp' or userInput == 'all':
            packageMode = userInput
            if packageMode == 'sp':
                userInput = input("Please enter a valid Package ID (example '1' or '10'):\n")
                if packageHashMap.verifyNode(int(userInput)):
                    package = packageHashMap.getNodeObject(int(userInput))
                else:
                    print("ERROR: Package ID does not exist exiting application now")
                    exit()
            userInput = input("To check package status at a specific time please enter 'time' or to check current status enter 'cs':\n")
            if userInput == 'time':
                time = timeConversion()
                if packageMode == 'sp':
                    package.verifyStatus(time)
                    print(package)
                if packageMode == 'all':
                    for x in range(1, packageHashMap.getTotalNodeCount()+1): # adds 1 so loop will start at packageID 1 and continue to max packageID
                        selectedNode = packageHashMap.getNodeObject(x) # Takes advantage of the fact that PackageID's are contiguous and sequentially ordered
                        selectedNode.verifyStatus(time)
                        print(selectedNode)
            elif userInput == 'cs' and packageMode == 'sp':
                print(package)
            elif userInput == 'cs' and packageMode == 'all':
                packageHashMap.print()
            else:
                print("ERROR: invalid input exiting applicaiton now")
                exit()
        else:
            print("ERROR: Invalid input exiting application")
            exit()
    except ValueError:
        print("ERROR: Invalid Input exiting application")
        exit()
            

if __name__ == "__main__":
    main()