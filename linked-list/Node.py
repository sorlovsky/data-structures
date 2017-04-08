class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def to_str(self):
        print(self.value)

    def print_list(self):
        current = self
        while current.next:
            print(current.value)
            current = current.next

    def addNode(self, node):
        current = self
        while current.next:
            current = current.next
        current.next = node

    def insertNode(self, node, index):
        current = self
        for i in range(index):
            current = current.next

        node.next = current.next
        current.next = node 

    def remove(self, node, index):
        pass

    def sort(self, node):
        pass

node = Node(1)
for i in range(10):
   node.addNode(Node(i)) 

node.insertNode(Node(99), 0) 
node.print_list()


