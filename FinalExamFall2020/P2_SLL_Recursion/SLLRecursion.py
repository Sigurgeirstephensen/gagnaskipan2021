class sll_node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

##########################   helper functions are encouraged in these problems   ##########################

def is_asc_desc_ordered(head):

    if check_asc(head) == False:
        if check_desc(head)==True:
            return True
        else:
            return False
    else:
        return True

def check_asc(head):
    if head == None:
        return False
    elif head.next == None:
        return True
    
    else:
        if head.next.value == head.value +1 :
            return check_asc(head.next)
        else:
            return False

def check_desc(head):
    if head == None:
        return False
    elif head.next == None:
        return True
    
    else:
        if head.next.value == head.value-1 :
            return check_desc(head.next)
        else:
            return False

def count_ascending_series(head):
    return count_ascending_series_helper(head, head.value)

def count_ascending_series_helper(head, prev_value):
    if head == None:
        return 1
    if head.value < prev_value:
        return 1 + count_ascending_series_helper(head.next, head.value)
    return 0 + count_ascending_series_helper(head.next, head.value)

if __name__ == "__main__":
    # print("is_asc_desc_ordered tests:")
    # test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    # print(is_asc_desc_ordered(test_head))
    # test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    # print(is_asc_desc_ordered(test_head))
    # test_head = sll_node(1, sll_node(3, sll_node(2, None))) #1,3,2
    # print(is_asc_desc_ordered(test_head))

    print("\ncount_ascending_series tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(count_ascending_series(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(2, sll_node(3, sll_node(2, sll_node(3, sll_node(4, sll_node(2, sll_node(7, sll_node(8, None))))))))) #1,2,3,2,3,4,2,7,8
    print(count_ascending_series(test_head))
    test_head = sll_node(5, sll_node(4, sll_node(3, sll_node(2, sll_node(1, None))))) #5,4,3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(1, sll_node(1, sll_node(2, sll_node(1, None))))) #1,1,1,2,1
    print(count_ascending_series(test_head))
