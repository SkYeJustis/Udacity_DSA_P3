def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not isinstance(input_list, list):
        return None

    current_pos_0 = 0
    current_pos_2 = len(input_list) - 1
    current_pos = 0

    while current_pos <= current_pos_2:
        if input_list[current_pos] == 0:
            input_list[current_pos] = input_list[current_pos_0]
            input_list[current_pos_0] = 0
            current_pos_0 += 1
            current_pos += 1
        elif input_list[current_pos] == 2:
            input_list[current_pos] = input_list[current_pos_2]
            input_list[current_pos_2] = 2
            current_pos_2 -= 1
        elif input_list[current_pos] == 1:
            current_pos += 1

    return input_list

if __name__ == '__main__':

    def test_function(test_case):
        sorted_array = sort_012(test_case)
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")

    # Scrambled list
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    # Long scrambled list
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    # Already ordered list
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # Invalid input
    print("Pass" if sort_012(12) == None else "Fail")
    print("Pass" if sort_012(None) == None else "Fail")
    print("Pass" if sort_012("invalid") == None else "Fail")

    # Very short list
    test_function([0])