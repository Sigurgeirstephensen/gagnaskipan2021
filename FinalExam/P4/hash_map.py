class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key=None, data=None, next=None, prev=None):
        self.key = key
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class Bucket:
    def __init__(self):
        self.header = Node()
        self.tailer = Node()
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0

    def add(self, key, value):
        new_node = Node(key, value, self.header.next, self.header)
        self.header.next.prev = new_node
        self.header.next = new_node
        self.size += 1

    def find(self, key, change_node=False):
        node = self.header.next
        while node is not self.tailer:
            if node.key == key:
                if change_node:
                    return node
                else:
                    return True
            node = node.next
        return False

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node is not self.tailer:
            ret_str += str("{}: {}, ".format(node.key, node.data))
            node = node.next
        return ret_str


class HashMap:
    def __init__(self):
        self.map = [Bucket() for _ in range(16)]

    def __setitem__(self, key, data):
        bucket_index = hash(key) % 16
        if self.map[bucket_index].find(key):
            node = self.map[key].find(key, True)
            node.data = data
        else:
            self.map[bucket_index].add(key, data)

    def __getitem__(self, key):
        bucket_index = hash(key) % 16
        if self.map[bucket_index].find(key):
            return self.map[bucket_index].find(key, True)
        else:
            raise NotFoundException

    def __len__(self):
        self.size = 0
        for x in self.map:
            self.size += x.size
        return self.size


if __name__ == "__main__":

    print("\nTESTING HASHMAP - MAKE BETTER TESTS!!")

    m = HashMap()
    m[3] = "Value for key: 3"
    m[6] = "Value for key: 6"
    m[2] = "Value for key: 2"


    print("")
    try:
        print(str(m[2]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[3]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[4]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[5]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[6]))
    except(NotFoundException):
        print("Item not found")
    print("Size of collection: " + str(len(m)))


    m[3] = "HELLOOO"
    print(m[3])


