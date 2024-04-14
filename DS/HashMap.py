# Hash Map Implementation
from DS.DLL import DLL

class HashMap:
    def __init__(self):
        self.size = 16 # Sets size of the hash map
        self.map = [None] * self.size # Initializes an empty array of null objects

    # Generates hash index based on PackageID
    def getHash(self, key):
        hash = key % self.size
        return hash

    def add(self, key, data):
        hashIndex = self.getHash(key)

        if self.map[hashIndex] == None: # Executes if hash map index is empty
            self.map[hashIndex] = DLL() # Creates a new DLL obj and stores it in Hash Map index
            DLL.PushFront(self=self.map[hashIndex], NewData=data)
        else:
            entry = self.map[hashIndex] # Retrieves DLL obj stored at Hash Map index
            entry.PushFront(data) # Adds new entry to DLL obj stored at Hash Map index

    # Retrieves Data stored in DLL by referencing PackageID variable (key)
    def get (self, key):
        hashIndex = self.getHash(key)

        if self.map[hashIndex] is None:
            return self.map[hashIndex]
        else:
            entry = self.map[hashIndex]
            return entry.GetNodeData(key) # "key" is the PackageID

    def delete(self, key):
        hashIndex = self.getHash(key)

        if self.map[hashIndex] is None:
            print("ERROR: Targeted hash map index is empty OR Package ID does not exist.")
            return
        else:
            entry = self.map[hashIndex]
            entry.DeleteNode(key)
            print("SUCCESS: Targted node was deleted.")

    # Prints Entire hash map
    def print(self):
        for item in range(self.size):
            if self.map[item] is not None:
                entry = self.map[item]
                entry.Print()
            else:
                print(self.map[item])

    # Verified the existence of a targeted Node
    def verifyNode(self, key):
        hashIndex = self.getHash(key)

        if self.map[hashIndex] is None:
            print("ERROR: Targeted Node does not exist")
        else:
            entry = self.map[hashIndex]
            if entry.GetNodeObject(key) is not None:
                print("SUCCESS: Targeted Node does exist")