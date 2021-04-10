
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = Node()
        self.tailer = Node()
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.curr = self.tailer
        self.size = 0

    def insert(self, data):
        node = Node(data, self.curr.prev, self.curr)
        node.prev.next = node
        node.next.prev = node
        self.curr = node
        self.size += 1

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove(self):
        if self.curr != self.tailer:
            self._remove(self.curr)
            self.curr = self.curr.next

    def get_value(self):
        if self.curr != self.tailer:
            return self.curr.data
        return None

    def _move_to_next(self):
        self.curr = self.curr.next

    def _move_to_prev(self):
        self.curr = self.curr.prev

    def move_to_next(self):
        if self.curr != self.tailer:
            self._move_to_next()

    def move_to_prev(self):
        if self.curr.prev != self.header:
            self._move_to_prev()

    def move_to_pos(self, pos):
        if pos < 0 or pos > self.size:
            return
        self.curr = self.header.next
        for _ in range(pos):
            self.curr = self.curr.next

    def clear(self):
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0
        self.curr = self.tailer

    def get_first_node(self):
        if self.size != 0:
            return self.header.next

    def get_last_node(self):
        if self.size != 0:
            return self.tailer.prev

    def partition(self, low, high):
        node = low.next
        while node != high.next:
            if node.data < low.data:
                self.curr = node
                val = self.curr.data
                self.remove()
                self.curr = low
                self.insert(val)
            node = node.next
        self.curr = low

    def sort(self):
        if self.size > 0:
            self.quicksort(self.get_first_node(), self.get_last_node())
        self.curr = self.header.next

    def quicksort(self, low, high):
        high_cache = high.next
        low_cache = low.prev
        self.partition(low, high)
        low = low_cache.next
        high = high_cache.prev

        if low is not self.curr:
           self.quicksort(low, self.curr.prev)
        if high is not self.curr:
           self.quicksort(self.curr.next, high)


    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
