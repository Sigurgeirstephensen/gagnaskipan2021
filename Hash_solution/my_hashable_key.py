
class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.i = int_value
        self.s = string_value
    
    def __eq__(self, other):
        return self.i == other.i and self.s == other.s

    def __hash__(self):
        # This is cheating, as students are
        # not allowed to use the built in hash functions
        # Besides, the python hash gives negative values
        # and random seeds between processes
        return abs(hash(self.i) + hash(self.s))