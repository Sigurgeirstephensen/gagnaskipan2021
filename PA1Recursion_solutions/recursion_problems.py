
def less_than(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    if b == 0:
        return False
    elif a == 0:
        return True
    return less_than(a - 1, b - 1)


def linear_search(list, value):
    if list == []:
        return False
    if list[0] == value:
        return True
    return linear_search(list[1:], value)

def unique_rec(lis1, unique_lis):
    if lis1 == []:
        return None
    if not linear_search(unique_lis, lis1[0]):
        unique_lis.append(lis1[0])
    unique_rec(lis1[1:], unique_lis)

def unique(lis1):
    ret_lis = []
    unique_rec(lis1, ret_lis)
    return ret_lis


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_less_than(num1, num2):
    if(less_than(num1, num2)):
        print(str(num1) + " is less than " + str(num2))
    else:
        print(str(num1) + " is NOT less than " + str(num2))

def test_unique(lis1):
    print(str(unique(lis1)) + " are the unique items in " + str(lis1))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_less_than(8, 3)
    test_less_than(2, 9)
    test_less_than(4, 17)
    test_less_than(11, 3)
    test_less_than(8, 2)
    test_less_than(8, 7)
    test_less_than(7, 8)
    test_less_than(6, 16)
    test_less_than(7, 7)

    print("\nTESTING HOW MANY:\n")

    test_unique(['a', 'f', 'd', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'b', 'f', 'g', 'a', 't', 'c', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['f', 'g', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    test_unique(['t'])


if __name__ == "__main__":
    run_recursion_program()