class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index > self.size or index < 0:
            raise IndexOutOfBounds()
        if self.size >= self.capacity:
            self.resize()
        i = self.size
        while(i > index):
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index >= 0 and index < self.size:
            self.arr[index] = value
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(0)

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size > index and index >= 0:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(self.size - 1)

    #Time complexity: O(n) - linear time in size of list (but doesn't change time complexity of append or insert)
    def resize(self):
        tmp_arr = [0] * self.capacity * 2
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity *= 2

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.size > index and index >= 0:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i + 1]
            self.size -= 1
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0

    def fill_sub_recursive(self, sub, current, end):
        if current == end:
            return sub
        sub.append(self.arr[current])
        return self.fill_sub_recursive(sub, current + 1, end)

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        if (start < 0) or (start + length > self.size):
            raise IndexOutOfBounds()
        sub = ArrayList(length)
        return self.fill_sub_recursive(sub, start, start + length)

    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        concat = ArrayList(self.size + other.size)
        concat = self.fill_sub_recursive(concat, 0, self.size)
        return other.fill_sub_recursive(concat, 0, other.size)
