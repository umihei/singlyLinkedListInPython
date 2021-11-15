class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)

        if(not self.head):
            self.head = newNode
            self.tail = newNode

        else:

            self.tail.next = newNode
            self.tail = newNode

        self.length = self.length + 1

        return self

    def traversal(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next

    def pop(self):

        if(not self.head):
            return None

        current = self.head
        newTail = current
        while(current.next):
            newTail = current
            current = current.next
        
        self.tail = newTail
        self.tail.next = None
        self.length = self.length + 1
        if (self.length == 0):
            self.head = None
            self.tail = None

        return current

    def shift(self):

        if(not self.head):
            return None

        current = self.head
        self.head = current.next
        self.length = self.length - 1
        if(self.length == 0):
            self.tail = None

        return current

    def unshift(self, val):

        newNode = Node(val)

        if(not self.head):
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head = newNode

        self.length = self.length + 1
        return self

    def get(self, index):
        if ((index < 0) or (index >= self.length)):
            return None
        counter = 0
        current = self.head
        while(counter != index):
            current = current.next
            counter = counter + 1

        return current

    def set(self, index, val):
        targetNode = self.get(index)
        if(not targetNode):
            return False
        else:
            targetNode.val = val
            return True

    def insert(self, index, val):
        if ((index < 0) or (index > self.length)):
            return False

        elif (index == self.length):
            return bool(self.push(val))

        elif (index == 0):
            return bool(self.unshift(val))

        else:
            newNode = Node(val)
            backNode = self.get(index - 1)
            frontNode = backNode.next
            backNode.next = newNode
            newNode.next = frontNode
            return True

    def remove(self, index):
        if ((index < 0) or (index >= self.length)):
            return None

        elif (index == (self.length - 1)):
            return self.pop()

        elif (index == 0):
            return self.shift()

        else:
            backNode = self.get(index - 1)
            targetNode = backNode.next
            backNode.next = targetNode.next
            self.length = self.length - 1
            return targetNode

    def printList(self):
        arr = list()
        current = self.head
        while(current):
            arr.append(current.val)
            current = current.next
        print(arr)

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        next = None
        prev = None
        for ii in range(0, self.length - 1):
            next = node.next
            node.next = prev
            prev = node
            node = next

        return self

singlyList = SinglyLinkedList()
singlyList.push(4)
singlyList.push(6)
singlyList.push(7)
singlyList.push(8)
singlyList.push(9)
singlyList.traversal()
print(singlyList.get(2))
print(singlyList.get(1).val)
singlyList.printList()
singlyList.pop()
singlyList.traversal()
singlyList.set(1,7)
singlyList.traversal()
print('')
singlyList.insert(1,5)
singlyList.traversal()
print('')
singlyList.remove(1)
singlyList.traversal()
print('')
singlyList.shift()
singlyList.traversal()
print('')
singlyList.unshift(4)
singlyList.traversal()
print('')
singlyList.reverse()
singlyList.traversal()