
class ModifiedTokenizer:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 0

        def get_next_token(self):
            ret_val = self.statement[self.position]
            self.position += 1

            return ret_val

class GT_Node:
    def __init__(self):
        self.name = ""
        self.children = []

def parse_bracket_file(filename):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    input_file = open(filename)
    t = ModifiedTokenizer(str(input_file.readline()))
    t.get_next_token()
    root = parse_recur(GT_Node(), t)

def parse_recur(node, token):
    while True:
        t = token.get_next_token()
        if t == "{":
            child_node = parse_recur(GT_Node(), token)
            node.children.append(child_node)
        elif t == "}":
            return node
        else:
            node.name += t

        
    


    

def write_bulleted_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")

def write_labelled_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    bullet_list_tree = parse_bracket_file("bracket_file_01.txt")
    write_bulleted_file("bullet_file_01.txt", bullet_list_tree)
    write_labelled_file("label_file_01.txt", bullet_list_tree)
