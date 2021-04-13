class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_front(self, value):
        new_node = Node(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node

    def push_back(self, value):
        new_node = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def pop_front(self):
        ret_value = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return ret_value

    def pop_back(self):
        ret_value = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return ret_value

    def traverse_back(self, head):
        if head.next.data is None:
            return str(head.data)
        else:
            return str(head.data) + " " + self.traverse_back(head.next)

    def traverse_front(self, node):
        if node.prev.data is None:
            return str(node.data)
        else:
            return str(node.data) + " " + self.traverse_front(node.prev)

    def find(self, target, node):
        if node is None:
            return False
        if node.data == target:
            return True
        else:
            return self.find(target, node.next)

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.data is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


my_dll = DLL()
my_dll.push_front(1)
my_dll.push_front(2)
my_dll.push_front(3)
my_dll.push_front(4)
my_dll.push_back(5)
print(my_dll)
print(my_dll.pop_front())
print(my_dll)
print(my_dll.pop_back())
print(my_dll)
print(my_dll.traverse_back(my_dll.head.next))
print(my_dll.traverse_front(my_dll.tail.prev))
print(my_dll.find(5, my_dll.head))