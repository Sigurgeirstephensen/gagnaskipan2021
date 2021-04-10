class HashTable:
    def __init__(self):
        self.capacity = 16
        self.bucket_list = []
        for i in range(self.capacity):
            self.bucket_list.append([])
    
    def insert(self, key):
        hash_val = hash(key)
        index = hash_val % self.capacity
        if key not in self.bucket_list[index]:
            self.bucket_list[index].append(key)

    def contains(self, key):
        hash_val = hash(key)
        index = hash_val % self.capacity
        if key in self.bucket_list[index]:
            return True
        return False

    def remove(self, key):
        hash_val = hash(key)
        index = hash_val % self.capacity
        if key in self.bucket_list[index]:
            self.bucket_list[index].remove(key)



class PrefixParsingTreeNode:
    def __init__(self, token, left, right):
        self.token = token
        self.left = left
        self.right = right

class PrefixParsingTree:
    def __init__(self):
        self.root = None

    class Tokenizer:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 0

        def get_next_token(self):
            i = self.position
            while i < len(self.statement) and self.statement[i] != " ":
                i += 1
            ret_val = self.statement[self.position:i]
            self.position = i + 1
            return ret_val

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()

        if token == "+" or token == "-":
            return PrefixParsingTreeNode(token, self.build_tree_recursive(tokenizer), self.build_tree_recursive(tokenizer))
        elif token.isdigit():
            return PrefixParsingTreeNode(token, None, None)
        else:
            return PrefixParsingTreeNode(token, None, None)

    def load_statement_string(self, statement):
        tokenizer = self.Tokenizer(statement)
        self.root = self.build_tree_recursive(tokenizer)

    def node_value_recursive(self, node):
        if node.left == None or node.right == None:
            return int(node.token)
        if node.token == "+":
            return self.node_value_recursive(node.left) + self.node_value_recursive(node.right)
        elif node.token == "-":
            return self.node_value_recursive(node.left) - self.node_value_recursive(node.right)

    def calculate_value(self):
        return self.node_value_recursive(self.root)



class BulletListNode:
    def __init__(self):
        self.string = None
        self.children = []

def parser_bracket_string_recursive(current_node, bracket_string, string_index):
    current_bullet_string = ""
    while True:
        if bracket_string[string_index] == "{":
            next_node = BulletListNode()
            current_node.children.append(next_node)
            string_index = parser_bracket_string_recursive(next_node, bracket_string, string_index + 1)
        elif bracket_string[string_index] == "}":
            current_node.string = current_bullet_string
            return string_index + 1
        else:
            current_bullet_string += bracket_string[string_index]
            string_index += 1
    

def parse_bracket_file(filename):
    input_file = open(filename)
    bracket_string = input_file.readline()
    i = 0
    while bracket_string[i] != "{":
        i += 1
    root = BulletListNode()
    parser_bracket_string_recursive(root, bracket_string, i+1)

    return root

def write_bullets_recursive(output_file, node, level):
    for child in node.children:
        for _ in range(level):
            output_file.write("\t")
        output_file.write(child.string + "\n")
        write_bullets_recursive(output_file, child, level + 1)

def write_bulleted_file(filename, my_tree):
    output_file = open(filename, "w")
    write_bullets_recursive(output_file, my_tree, 1)

def write_label_list_recursive(output_file, node, level):
    for i in range(len(node.children)):
        child = node.children[i]
        for _ in range(level):
            output_file.write("\t")
        if level == 0:
            output_file.write(str(i + 1) + ".\t")
        elif level == 1:
            output_file.write(chr(ord("a") + i) + ")\t")
        else:
            output_file.write("-\t")
        output_file.write(child.string + "\n")
        write_label_list_recursive(output_file, child, level + 1)

def write_labelled_file(filename, my_tree):
    output_file = open(filename, "w")
    write_label_list_recursive(output_file, my_tree, 0)

def test_hash_table():
    t = HashTable()
    t.insert("test1")
    t.insert("test2")
    t.insert("test3")
    t.insert("test1")
    print(t.contains("test3"))
    print(t.contains("test1"))
    print(t.contains("test4"))
    t.remove("test3")
    print(t.contains("test3"))
    t.remove("test1")
    print(t.contains("test2"))
    print(t.contains("test1"))

def test_prefix_tree(statement_string):
    print("This is the statement: " + statement_string)
    ppt = PrefixParsingTree()
    ppt.load_statement_string(statement_string)
    print("This is the result: " + str(ppt.calculate_value()))



# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    print("testing hash table")
    test_hash_table()

    print("testing prefix tree")
    test_prefix_tree("- 12 + 4 5")
    test_prefix_tree("+ 12 + - 21 5 5")
    test_prefix_tree("+ 4 + - 4 6 - 9 8")
    test_prefix_tree("- + - + 6 9 8 + 1 + 5 5 - - + 6 7 - 9 8 - + 9 6 1")
    test_prefix_tree("+ + 8 4 - + - 3 3 2 - + 7 8 9")


    bullet_list_tree = parse_bracket_file("bracket_file_01.txt")
    write_bulleted_file("bullet_file_01.txt", bullet_list_tree)
    write_labelled_file("label_file_01.txt", bullet_list_tree)

    
