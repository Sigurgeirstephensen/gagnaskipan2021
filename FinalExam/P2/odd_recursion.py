# TODO: Implement the operation print_odd here
def _odd_help(num):
    if num == 0:
        return ""
    if num % 2 == 1:
        return str(_odd_help(num - 1)) + " " + str(num)
    else:
        return str(_odd_help(num - 1))


def print_odd(num):
    print(_odd_help(num))


if __name__ == "__main__":
    print("TESTING PRINT_ODD - MAKE BETTER TESTS!!!\n")

    print_odd(16)
    print_odd(15)
    print_odd(17)
