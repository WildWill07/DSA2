# Doubly Linked List Implementation
# DLL used for collision chaining in hash map
from Node import PackageNode

class DLL:
    def __init__(self):
        self.head = None # Point to Null when list is empty
        self.tail = None

    def PushFront(self, NewData):
        NewNode = PackageNode(NewData)
        NewNode.next = self.head # Newly created node will point to the old 'head' node

        if self.head != None: # Executes if list DLL is populated
            self.head.prev = NewNode
            self.head = NewNode
            NewNode.prev = None

        else: # Executs if DLL is Empty
            self.head = NewNode
            self.tail = NewNode
            NewNode.prev = None

    def PushBack(self, NewData):
        NewNode = PackageNode(NewData)
        NewNode.prev = self.tail

        if self.tail == None: # Executes if the DLL is empty
            self.head = NewNode
            self.tail = NewNode
            NewNode.next = None

        else: # Executes if DLL is not empty
            self.tail.next = NewNode
            NewNode.next = None
            self.tail = NewNode # Sets new Node as last element in DLL

    def Print(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next

testDLL = DLL()
myTuple1 = (1, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")
myTuple2 = (2, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")
myTuple3 = (3, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")

testDLL.PushFront(NewData=myTuple1)
testDLL.PushFront(NewData=myTuple2)
testDLL.PushFront(NewData=myTuple3)

testDLL.Print()

# Methods for DLL: 
# 
# PushFront - DONE
# PushBack - DONE
# GetNode
# Print - DONE
# Delete
# PopFront
# PopBack
# InsertBefore
# InsertAfter