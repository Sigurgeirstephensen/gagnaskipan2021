class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.left == None:
            return str(self.value)
        else:
            return str(self.value) + "(" + str(self.left) + "," + str(self.right) + ")"

class BooleanTree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return str(self.root)

    def _build_node_recur(self, values):
        value = values.pop()
        ret_node = TreeNode(value)
        if value == "AND" or value == "OR":
            ret_node.left = self._build_node_recur(values)
            ret_node.right = self._build_node_recur(values)
        elif value == "T":
            ret_node.value = True
        elif value == "F":
            ret_node.value = False
        return ret_node

    def build_tree(self, statement_string):
        values_preorder_reversed = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
        values_preorder_reversed.reverse()
        self.root = self._build_node_recur(values_preorder_reversed)

    def _get_node_value_recur(self, node):
        if node.left == None:
            return node.value
        else:
            if node.value == "AND":
                return self._get_node_value_recur(node.left) and self._get_node_value_recur(node.right)
            elif node.value == "OR":
                return self._get_node_value_recur(node.left) or self._get_node_value_recur(node.right)

    def get_root_value(self):
        return self._get_node_value_recur(self.root)


if __name__ == "__main__":

    print("\nSHOWING HOW TO LOSE THE DELIMITERS, IF WANTED")
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    # YOU CAN DO THIS IN YOUR build_tree() OPERATION IF THE LIST FORMAT FEELS BETTER
    statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
    print(statement_list)


    print("\n\nTESTING BOOLEAN TREE\n")

    # THESE TESTS SHOULD WORK EXACTLY AS THEY ARE BUT FEEL FREE TO MAKE MORE EXTENSIVE TESTS AS WELL

    bt = BooleanTree()
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(T,AND(T,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(AND(T,T),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(T,OR(F,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(F,T),T)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(F,F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(OR(F,F),T),OR(T,AND(T,F)))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())