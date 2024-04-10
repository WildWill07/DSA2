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

    def InsertBefore(self, ID, NewData):
        currentNode = DLL.GetNodeObject(self, id=ID)

        if currentNode == None:
            DLL.ErrorMessage_NullNode()
            return
        else:
            if currentNode.prev == None: # Executes if the insert before Node is the head Node
                DLL.PushFront(NewData)
            else:
                NewNode = PackageNode(NewData)
                NewNode.prev = currentNode.prev # Points NewNode prev to the prev node of the insert before node
                NewNode.next = currentNode # Points NewNode next to the insert before node
                currentNode.prev = NewNode
                NewNode.prev.next = NewNode


    def InsertAfter(self, ID, NewData):
        currentNode = DLL.GetNodeObject(self, id=ID)
        
        if currentNode == None:
            DLL.ErrorMessage_NullNode()
            return
        else:
            if currentNode.next == None: # Executes if the insert after node is the tail node
                DLL.PushBack(NewData)
            else:
                NewNode = PackageNode(NewData)
                NewNode.next = currentNode.next # Points NewNode next to the insert after nodes next node pointer
                NewNode.prev = currentNode # Points NewNode prev pointer to the insert after node object
                currentNode.next = NewNode # Points insert after node next pointer to the NewNode object
                NewNode.next.prev = NewNode # Points the NewNode next node's prev node pointer to the NewNode object


    def Print(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
        if self.head == None and self.tail == None:
            print("The DLL is empty.")

    def GetNodeData(self, id): # Retruns specific PackageNode by referencing PackageID
        self.ID = id
        currentNode = self.head
        
        while currentNode.PackageID != self.ID: # Exits when desired node is found or returns Null when entire DLL is traversed
            currentNode = currentNode.next
            if currentNode == None:
                DLL.ErrorMessage_NullNode()
                return None
            
        return currentNode.data
    
    def PeekFront(self): # Returns data tuple of head node object
        if self.head == None:
            DLL.ErrorMessage_EmptyList()
            return
        else:
            return self.head.data

    def PeekBack(self): # Returns data tuple of tail node object
        if self.tail == None:
            DLL.ErrorMessage_EmptyList()
            return
        else:
            return self.tail.data
    
    def GetNodeObject(self, id): # Retruns specific PackageNode by referencing PackageID
        self.ID = id
        currentNode = self.head
        
        while currentNode.PackageID != self.ID: # Exits when desired node is found or returns Null when entire DLL is traversed
            currentNode = currentNode.next
            if currentNode == None:
                DLL.ErrorMessage_NullNode()
                return None
            
        return currentNode

    def DeleteNode(self, id): # Removes a specific node by referencing PackageID
        self.ID = id
        currentNode = self.head

        while currentNode.PackageID != self.ID:
            currentNode = currentNode.next
            if currentNode == None:
                DLL.ErrorMessage_NullNode()
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
            DLL.ErrorMessage_EmptyList()
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
            DLL.ErrorMessage_EmptyList()
            return None
        
    def ErrorMessage_EmptyList():
        print("ERROR: Cannot perform action as the list is empty.")

    def ErrorMessage_NullNode():
        print("ERROR: The targeted node does not exist.")