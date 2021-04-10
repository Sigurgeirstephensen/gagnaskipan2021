
class Node:
    def __init__(self, data="", parent=None):
        self.data = data
        self.parent = parent
        self.children = []


def parse_bracket_file(filename):
    input_file = open(filename)
    root = current = None

    for symbol in input_file.readline():
        if symbol == "{":
            new_node = Node("", current)
            if root == None:
                root = current = new_node
            else:
                current.children.append(new_node)
                current = new_node
        elif symbol == "}":
            current = current.parent
        else:
            current.data += symbol

    input_file.close()

    return root


def write_bulleted_file(filename, my_tree):
    output_file = open(filename, "w")
    __write_bulleted(output_file, my_tree)
    output_file.close()


def __write_bulleted(output_file, current, depth=1):
    if current == None:
        return
    for child in current.children:
        output_file.write("\t" * depth + child.data + "\n")
        __write_bulleted(output_file, child, depth+1)


def write_labelled_file(filename, my_tree):
    output_file = open(filename, "w")
    __write_labelled(output_file, my_tree)
    output_file.close()


def __write_labelled(output_file, current, depth=1):
    if current == None:
        return
    counter = 1
    letter_counter = 97
    for child in current.children:
        if depth == 1:
            output_file.write(str(counter) + ".")
            counter += 1
        elif depth == 2:
            output_file.write("\t" + chr(letter_counter) + ")")
            letter_counter += 1
        else:
            output_file.write("\t" * (depth-1) + "-")
        output_file.write("\t" + child.data + "\n")
        __write_labelled(output_file, child, depth+1)


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    bullet_list_tree = parse_bracket_file("bracket_file_01.txt")
    write_bulleted_file("bullet_file_01.txt", bullet_list_tree)
    write_labelled_file("label_file_01.txt", bullet_list_tree)
