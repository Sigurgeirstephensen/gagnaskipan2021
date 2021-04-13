class btNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + " "


class TreeClass:
    def __init__(self, preset=0):
        self.size = 0
        self.root = None
        self.preset = preset
        if self.preset == 1:
            self.listOfNodes = [5, 2, 4, 1, 8, 7, 9]
        elif self.preset == 2:
            self.listOfNodes = ['c', 'a', 'b', 'e', 'd', 'f']
        elif self.preset == 3:
            self.listOfNodes = [20, 13, 8, 15, 27, 21]
        else:
            self.listOfNodes = []

        if self.preset != 0:
            self._make_tree()

    def _make_tree(self):
        for obj in self.listOfNodes:
            self.insert(obj, "")

    def insert(self, key, value):
        self.size += 1
        if self.root is None:
            self.root = btNode(key, value)
        else:
            self._insert(key, value, self.root)

    def _insert(self, key, value, node):
        if key < node.key:
            if node.left:
                self._insert(key, value, node.left)
            else:
                node.left = btNode(key, value)
        if key > node.key:
            if node.right:
                self._insert(key, value, node.right)
            else:
                node.right = btNode(key, value)

    def _inorder(self, node):
        my_str = ""
        if node:
            my_str += self._inorder(node.left)
            my_str += str(node)
            my_str += self._inorder(node.right)
        return my_str

    def _preorder(self, node):
        my_str = ""
        if node:
            my_str += str(node)
            my_str += self._preorder(node.left)
            my_str += self._preorder(node.right)
        return my_str

    def _postorder(self, node):
        my_str = ""
        if node:
            my_str += self._postorder(node.left)
            my_str += self._postorder(node.right)
            my_str += str(node)
        return my_str

    def _find(self, key, node):
        if node is None:
            return None
        if key == node.key:
            return node
        else:
            if key < node.key:
                return self._find(key, node.left)
            else:
                return self._find(key, node.right)

    def __setitem__(self, key, value):
        if self._find(key, self.root):
            self._find(key, self.root).value = value
        else:
            self.insert(key, value)

    def __getitem__(self, key):
        if self._find(key, self.root):
            return self._find(key, self.root).value
        else:
            return None

    def __str__(self):
        if self.size != 0:
            ret_string = self._preorder(self.root) + "\n" + self._inorder(self.root) + "\n" + self._postorder(self.root)
        else:
            ret_string = ""
        return ret_string


class HashClass:
    def __init__(self):
        self.mapSize = 16
        self.bucket = []
        self.map = [self.bucket[:] for _ in range(self.mapSize)]

    def add(self, key, value):
        self.map[hash(key) % self.mapSize] = value

    def __setitem__(self, key, value):
        self.map[hash(key) % self.mapSize] = value

    def __getitem__(self, key):
        if self.map[hash(key) % self.mapSize]:
            return self.map[hash(key) % self.mapSize]
        else:
            return None


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":
    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    """
    h = HashClass()
    h = HashClass(1)
    """
    """
    t = TreeClass()
    t = TreeClass(1)
    """

"""
if __name__ == "__main__":
    print("\nTesting TreeClass __setitem & __getitem___")
    t = TreeClass()
    t[17] = "seventeen"
    t[3] = "three"
    t[23] = "twntythree"
    print(str(t[23]))
    t[23] = "twentythree"
    print(str(t[23]))
    print(str(t[3]))
    print(str(t[4]))
    print(str(t))
"""

"""
if __name__ == "__main__":
    print("\nTesting TreeClass __init__ & __str__")
    t = TreeClass()
    print("The tree: \n" + str(t))
    t = TreeClass(3)
    print("The tree: \n" + str(t))
    t = TreeClass(0)
    print("The tree: \n" + str(t))
"""

"""
if __name__ == "__main__":
    print("\nTesting HashClass: __setitem__ & __getitem__")
    h = HashClass()
    h[3] = "three"
    h[17] = "seventeen"
    h[23] = "twntythree"
    print(str(h[23]))
    h[23] = "twentythree"
    print(str(h[23]))
    print(str(h[3]))
    print(str(h[4]))
"""