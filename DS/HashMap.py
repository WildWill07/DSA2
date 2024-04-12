# Hash Map Implementation
from DLL import DLL

class HashMap:
    def __init__(self):
        self.size = 16 # Sets size of the hash map
        self.map = [None] * self.size # Initializes an empty array of null objects

    def getHash(self, key):
        hash = key % self.size # Takes the mod (size of the hash map) from the package ID and returns value as hash index
        return hash

    def add(self, key, value):
        pass

    def get (self, key):
        pass

    def delete(self, key):
        pass

    def print(self):
        pass