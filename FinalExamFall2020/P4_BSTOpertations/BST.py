class BinaryNode:
    def __init__(self, value=None, size=1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = size #defaults at 1 must be incremented inside insert functionality


    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += self.left.__str__()
        ret_str += "value: " + str(self.value) + " " + "size: " + str(self.size) + "\n"
        if self.right != None:
            ret_str += self.right.__str__()
        return ret_str

class BST:
    def __init__(self):
        self.root = None

    ############################## you can modify both insert and insert_recur functions ##############################
    ############################## but make sure not to change parameters of the insert function ##############################
    ############################## a fresh copy of these functions can be found below if you want a fresh start ##############################
    def insert(self, value):
        #if empty tree
        if self.root == None:
            self.root = BinaryNode(value)
        #else do normal recursive insert
        else:
            self.insert_recur(self.root, value)

    ############################## you can change these parameters to whatever you like ##############################
    def insert_recur(self, node, value):
        #if at a leaf we know the value doesn't exist
        #then we create a new node and return it
        if node == None:
            return BinaryNode(value)
        #if parameter value is smaller then current node value
        #we call the left side and make it our left side
        #then we return node at the end of the funciton
        elif node.value > value:
            node.left = self.insert_recur(node.left, value)
        #if parameter value is bigger then current node value
        #we call the right side and make it our right side
        #then we return node at the end of the funciton
        elif node.value < value:
            node.right = self.insert_recur(node.right, value)
        #here we are returning the current node. This happens both if we have a bigger or smaller value then the current node value
        return node
        
    def contains_value(self, value):
        return False
    
    #calls str function of root
    def __str__(self):
        if self.root == None:
            return ""
        else:
            return self.root.__str__()

    ############################## Here is a fresh copy of insert/insert_recur if you want to start fresh ##############################

    # def insert(self, value):
    #     #if empty tree
    #     if self.root == None:
    #         self.root = BinaryNode(value)
    #     #else do normal recursive insert
    #     else:
    #         self.insert_recur(self.root, value)

    # def insert_recur(self, node, value):
    #     #if at a leaf we know the value doesn't exist
    #     #then we create a new node and return it
    #     if node == None:
    #         return BinaryNode(value)
    #     #if parameter value is smaller then current node value
    #     #we call the left side and make it our left side
    #     #then we return node at the end of the funciton
    #     elif node.value > value:
    #         node.left = self.insert_recur(node.left, value)
    #     #if parameter value is bigger then current node value
    #     #we call the right side and make it our right side
    #     #then we return node at the end of the funciton
    #     elif node.value < value:
    #         node.right = self.insert_recur(node.right, value)
    #     #here we are returning the current node. This happens both if we have a bigger or smaller value then the current node value
    #     return node

if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(8)
    bst.insert(6)
    bst.insert(9),
    print(bst)
    bst.insert(9)
    print(bst) #here the size values shouldn't change
    #notice that in expected out there is no change in sizes after adding an already existing value ot the bst
    print(bst.contains_value(6))
    print(bst.contains_value(7))
    print(bst.contains_value(10))
    print(bst.contains_value(8))
