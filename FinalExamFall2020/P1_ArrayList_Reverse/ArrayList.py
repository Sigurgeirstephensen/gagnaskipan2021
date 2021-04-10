class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass



class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.is_ordered = True

    #################### you can use any already built functions in this class or build your own ####################
    #################### make sure not to break previously working operations ####################

    def reverse_list(self):
        for i in range(0, self.size//2):
            temp = self.arr[i]
            self.arr[i] = self.arr[self.size-(i+1)]
            self.arr[self.size-(i+1)] = temp

    #allows us to print this object
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    #adds an item to the front of the list
    def prepend(self, value):
        self.insert(value, 0)

    #adds an item at a specific index
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
        if self.size > 1:
            self.is_ordered = False

    #adds to the back of the list
    def append(self, value):
        self.insert(value, self.size)

    #set a value at index as value overwriting what the previous value was in that location
    def set_at(self, value, index):
        if index >= 0 and index < self.size:
            self.arr[index] = value
            if self.size > 1:
                self.is_ordered = False
        else:
            raise IndexOutOfBounds()
    
    #gets the item at the start of the list
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(0)

    #gets the item at a specific index
    def get_at(self, index):
        if self.size > index and index >= 0:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #gets the last item of the list
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(self.size - 1)

    #removed an item at index
    def remove_at(self, index):
        if self.size > index and index >= 0:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i + 1]
            self.size -= 1
            if self.size <= 1:
                self.is_ordered = True
        else:
            raise IndexOutOfBounds()
    
    #internal function should not be called
    #used for resizing the array
    def resize(self):
        tmp_arr = [0] * self.capacity * 2
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity *= 2

if __name__ == "__main__":
    lis = ArrayList()
    lis.append(3)
    lis.append(2)
    lis.append(1)
    print(lis)
    lis.reverse_list()
    print(lis)
    lis.append(4)
    lis.append(5)
    print(lis)
    lis.reverse_list()
    print(lis)
