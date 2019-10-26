def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not isinstance(input_list, list):
        return [None, None]

    size = len(input_list)

    if size == 0:
        return [None, None]
    if size == 1:
        return [None, None]

    sorted = mergesort(input_list)

    if size % 2 == 0:
        first_num = [sorted[i] for i in range(size-1, -1, -1) if i % 2 != 0]
        second_num = [sorted[i] for i in range(size-1, -1, -1) if i % 2 == 0]
    else:
        first_num = [sorted[-1]]
        for i in range(size-2, 0, -1):
            if i % 2 != 0:
                first_num.append(sorted[i])
        second_num = [sorted[i] for i in range(size-2, -1, -1) if i % 2 == 0]

    return [int("".join(map(str, first_num))), int("".join(map(str, second_num)))]

def mergesort(input_array):
    if len(input_array) <= 1:
        return input_array

    mid = len(input_array)//2
    left = input_array[:mid]
    right = input_array[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


if __name__ == '__main__':

    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")


    # Default tests
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


    # Invalid input
    print("Pass" if rearrange_digits(None) == [None, None] else "Fail")
    print("Pass" if rearrange_digits(11.1) == [None, None] else "Fail")
    print("Pass" if rearrange_digits([]) == [None, None] else "Fail")
    print("Pass" if rearrange_digits([1]) == [None, None] else "Fail")


    # Longer number strings with two digit numbers - odd list size
    test_function([[11, 6, 9, 10, 5, 7, 8], [111086, 975]])


    # Longer number strings with two digit numbers - even list size
    test_function([[40, 14, 5, 10, 2, 95], [95145, 40102]])
