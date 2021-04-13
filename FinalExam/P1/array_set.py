class ArraySet:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def _resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.arr[ix]
        self.arr = temp

    def add(self, value):
        if self.size + 1 == self.capacity:
            self._resize()
        self.arr[self.size] = value
        self.size += 1

    def sort_list(self):
        for x in range(self.size):
            lowest_value = x
            for y in range(x + 1, self.size):
                if self.arr[y] < self.arr[lowest_value]:
                    lowest_value = y
            self.arr[lowest_value], self.arr[x] = self.arr[x], self.arr[lowest_value]

    def no_dupes(self):
        new_arr = [None] * self.capacity
        for ix in range(self.size):
            if self.arr[ix] not in new_arr:
                new_arr[ix] = self.arr[ix]
        self.arr = new_arr

    def _count_list(self, my_list):
        if len(my_list) == 0:
            return 0
        if my_list[0] is None:
            return 0 + self._count_list(my_list[1:])
        else:
            return 1 + self._count_list(my_list[1:])

    def __str__(self):
        ret_str = ""
        self.no_dupes()
        self.size = self._count_list(self.arr)
        self.sort_list()
        for ix in range(self.size):
            ret_str += str(self.arr[ix]) + " "
        return ret_str


if __name__ == "__main__":
    print("\nTESTING ARRAY SET - MAKE BETTER TESTS!!\n")

    lis = ArraySet()
    lis.add(4)
    print(lis)
    lis.add(2)
    print(lis)

    lis.add(7)
    print(lis)

    lis.add(1)
    print(lis)

    lis.add(11)
    print(lis)

    lis.add(2)
    print(lis)

    lis.add(9)
    print(lis)
    lis.add(12)
    lis.add(13)
    lis.add(14)
    lis.add(15)
    lis.add(16)
    lis.add(16)
    print(lis)
