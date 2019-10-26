

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not isinstance(ints, list):
        return (None, None)

    if len(ints) == 0:
        return (None, None)
    if len(ints) == 1:
        return (None, ints[0])

    max = float('-inf')
    min = float('inf')

    for i in ints:
        if i > max:
            max = i
        if i < min:
            min = i

    if max == float('-inf'):
        max = None
    if min == float('inf'):
        min = None

    return (min, max)

"""
References:
    Udacity: Data Structures and Nanodegree Program - 3. Basic Algorithms
"""

if __name__ == '__main__':
    ## Example Test Case of Ten Integers
    import random

    # Default
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # Very large list
    l = [i for i in range(0, 90001)]  # a list containing 0 - 90000
    random.shuffle(l)
    print("Pass" if ((0, 90000) == get_min_max(l)) else "Fail")

    # A few non-sequential examples
    print("Pass" if ((5, 66) == get_min_max([66, 9, 5])) else "Fail")
    print("Pass" if ((10, 101) == get_min_max([101, 10, 99])) else "Fail")

    # Small example
    print("Pass" if ((2, 91) == get_min_max([91, 2])) else "Fail")
    print("Pass" if ((2, 91) == get_min_max([2, 91])) else "Fail")


    # Edge case - invalid types
    print("Pass" if ((None, None) == get_min_max(None)) else "Fail")
    print("Pass" if ((None, None) == get_min_max(12.1)) else "Fail")
    print("Pass" if ((None, None) == get_min_max([])) else "Fail")
    print("Pass" if ((None, 31) == get_min_max([31])) else "Fail")