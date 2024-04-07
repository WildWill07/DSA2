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

    def Print(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next

# Methods for DLL: 
# 
# PushFront - DONE
# PushBack
# GetNode
# Print - DONE
# Delete
# PopFront
# PopBack
# InsertBefore
# InsertAfter