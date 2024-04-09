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
        if self.head == None and self.tail == None:
            print("The DLL is empty.")

    def GetNode(self, id): # Retruns specific PackageNode by referencing PackageID
        self.ID = id
        currentNode = self.head
        
        while currentNode.PackageID != self.ID: # Exits when desired node is found or returns Null when entire DLL is traversed
            currentNode = currentNode.next
            if currentNode == None:
                DLL.ErrorMessage()
                return None
            
        return currentNode.data

    def DeleteNode(self, id): # Removes a specific node by referencing PackageID
        self.ID = id
        currentNode = self.head

        while currentNode.PackageID != self.ID:
            currentNode = currentNode.next
            if currentNode == None:
                DLL.ErrorMessage()
                return None
            
        currentNode.next.prev = currentNode.prev
        currentNode.prev.next = currentNode.next

    def PopFront(self): # Removes first Node in DLL or returns Null if DLL is empty
        if self.head != None: # Executes if DLL is populated
            currentNode = self.head
            if currentNode.next == None: # Executes if the DLL has only 1 element & sets DLL to an empty List
                currentNode.prev = None
                self.head = None
                self.tail = None
                return

            currentNode.next.prev = None
            self.head = currentNode.next
            currentNode.next = None

        else: # Executes if DLL is empty
            DLL.ErrorMessage()
            return None
        
    def PopBack(self): # Removes last Node in DLL or returns Null if DLL is empty
        if self.tail != None: # Executes if DLL is populated
            currentNode = self.tail
            if currentNode.prev == None: # Executes if the DLL has only 1 element & sets DLL to an empty List
                currentNode.next = None
                self.head = None
                self.tail = None
                return

            currentNode.prev.next = None
            self.tail = currentNode.prev
            currentNode.prev = None

        else: # Executs if DLL is empty
            DLL.ErrorMessage()
            return None
        
    def ErrorMessage():
        print("Cannot perform action as the list is empty.")

testDLL = DLL()
myTuple1 = (1, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")
myTuple2 = (2, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")
myTuple3 = (3, "195 W Oakland Ave", "Salt Lake City", 84115, "#######", 21, "HUB")

testDLL.PushFront(NewData=myTuple1)
testDLL.PushFront(NewData=myTuple2)
testDLL.PushFront(NewData=myTuple3)

# Methods for DLL: 
# 
# PushFront - DONE
# PushBack - DONE
# GetNode - DONE
# Print - DONE
# Delete - DONE
# PopFront - DONE
# PopBack - DONE
# InsertBefore
# InsertAfter

# ToDo
#
# Look into adding currentNode class variable to reduce method private current node declarations