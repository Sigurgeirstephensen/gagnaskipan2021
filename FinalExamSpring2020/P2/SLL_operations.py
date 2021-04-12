
class SLL_Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)
# IMPLEMENT HERE

def is_doubled(head1,head2):
    if head1 == None and head2 == None:
        return True
    elif head1== None or head1.next == None or head2 == None:
        return False
    elif head1.data != head2.data or head1.next.data != head2.data:
        return False
    return is_doubled(head1.next.next,head2.next)
    
if __name__ == "__main__":
    
    print("\n\nTESTING DOUBLED:\n")

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(7, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4)))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9)))
    print(is_doubled(head1, head2))
