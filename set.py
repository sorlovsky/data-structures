# 2016 December 25 by Simon A Orlovsky

class LinkedListNode(object):
    """A basic linked list node class, for use in implementing other more interesting classes."""
    
    def __init__(self, data):
        """Initializes a new node with the given data and no next node."""
        self.data = data
        self.next = None
    
    def setData(self, data):
        """Sets the node's data, which is set for the first time in __init__()."""
        self.data = data
    
    def getData(self):
        """Returns the data currently stored in the node."""
        return self.data
    
    def setNext(self, next):
        """Sets the next node, which is None by default."""
        self.next = next
    
    def getNext(self):
        """Returns the next node, or None."""
        return self.next

class Set(object):
    """Represents a set of objects. Any object is either in the set or not. The objects in the set don't have any particular order. In our Miller and Ranum textbook this class is called UnorderedList."""
    
    def __init__(self):
        """Initializes an empty set."""
        self.head = None
    
    def add(self, x):
        """Adds the given object x to the set. If the object is already in the set, then this has no effect."""
        if not self.has(x):
            temp = LinkedListNode(x)
            temp.setNext(self.head)
            self.head = temp
    
    def remove(self, x):
        """Removes the given object x from the set. If the object is not in the set, then this has no effect."""
        # Inchworm until we find x or the end of the linked list.
        current = self.head
        while current != None and current.getData() != x:
            previous = current
            current = current.getNext()
        if current != None:
            # We have found x; snip its node out of the linked list.
            if current == self.head:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
    
    def has(self, x):
        """Returns True or False based on whether the set contains the given object x."""
        current = self.head
        while current != None:
            if current.getData() == x:
                return True
            else:
                current = current.getNext()
        return False
    
    def getSize(self):
        """Returns the number of objects in the set."""
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def getElement(self):
        """If the set is not empty, then returns some object from the set. If the set is empty, then returns None."""
        if self.head == None:
            return None
        else:
            return self.head.getData()
    
    def __str__(self):
        """Returns a human-readable string representation of the set, assuming that the objects in the set themselves respond to the __str__ method."""
        if self.head == None:
            # There are no objects in the set.
            return "{}"
        elif self.head.getNext() == None:
            # There is exactly one object in the set.
            return "{" + str(self.head.getData()) + "}"
        else:
            # There are at least two objects; commas are needed.
            string = "{" + str(self.head.getData())
            current = self.head.getNext()
            while current != None:
                string += ", " + str(current.getData())
                current = current.getNext()
            string += "}"
            return string

# If this file was executed (rather than imported), then run this demo.
if __name__ == "__main__":
    mySet = Set()
    print mySet
    mySet.add("Jan")
    print mySet
    mySet.add("Jim")
    print mySet
    mySet.add(13)
    print mySet
    mySet.add(-37.44)
    print mySet
    mySet.add([12, "Joan"])
    print mySet
    mySet.add("Jan")
    print mySet
    mySet.add("Juanita")
    print mySet
    mySet.remove("Jim")
    print mySet
    mySet.remove("Jose")
    print mySet
    print mySet.has("Jan")
    print mySet.getSize()
