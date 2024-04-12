# Hash Map Implementation
from DLL import DLL
from Node import PackageNode

class HashMap:
    def __init__(self):
        self.size = 16 # Sets size of the hash map
        self.map = [None] * self.size # Initializes an empty array of null objects

    def getHash(self, key):
        hash = key % self.size # Takes the mod (size of the hash map) from the package ID and returns value as hash index
        return hash

    def add(self, key, data):
        hashIndex = self.getHash(key)

        if self.map[hashIndex] == None: # Executes if hash map index is empty
            self.map[hashIndex] = DLL()
            DLL.PushFront(data)
        else:
            DLL.PushFront(data)

    def get (self, key):
        pass

    def delete(self, key):
        pass

    def print(self):
        for item in self.map:
            if item is not None:
                pass
            # Rewrite this method possibly use in range for loop
