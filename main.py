from DS.HashMap import HashMap
from csvReader import PackageDataReader

def main():
    packageHashMap = HashMap()
    dataReader = PackageDataReader()

    dataReader.loadHashMap(packageHashMap)
    packageHashMap.print()

if __name__ == "__main__":
    main()