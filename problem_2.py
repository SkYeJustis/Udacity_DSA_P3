def binary_search(nlist, tgt):
    low = 0
    high = len(nlist) - 1

    while low <= high:
        pivot = (low + high) // 2
        if nlist[pivot] == tgt:
            return pivot
        elif nlist[pivot] > tgt:
            high = pivot - 1
        else:
            low = pivot + 1
    return -1

def rotated_index(nlist):
    low = 0
    high = len(nlist) - 1

    if nlist[low] < nlist[high]:
        return 0

    while low <= high:
        pivot = (low + high) // 2
        if nlist[pivot] > nlist[pivot + 1]:
            return pivot + 1
        elif nlist[pivot] < nlist[low]:
            high = pivot - 1
        else:
            low = pivot + 1

def rotated_array_search(nums, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not nums:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    rotate_index = rotated_index(nums)

    # Target is smallest
    if nums[rotate_index] == target:
        return rotate_index
    # No rotation
    if rotate_index == 0:
        return binary_search(nums, target)
    # Rotation detected
    else:
        if nums[0] > target:
            result = binary_search(nums[rotate_index:], target)
            result = result if result == -1 else result + rotate_index
        else:
            result = binary_search(nums[:rotate_index], target)
        return result

if __name__ == '__main__':
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        if linear_search(input_list, number) == rotated_array_search(input_list, number):
            print("Pass")
        else:
            print("Fail")

    # Default tests
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[6, 7, 8, 1, 2, 3, 4], 3])

    # No rotated array
    test_function([[1, 2, 3, 4, 7, 9, 1000, 100000], 1000])

    # Rotated array - large numbers
    test_function([[800, 999, 10000, 21, 45, 111, 200], 111])


    # Number not found
    test_function([[800, 999, 10000, 21, 45, 111, 200], 123])

    # One number list
    test_function([[1], 2])
    test_function([[1], 1])

    # Null list
    test_function([[None], 2])

    # Null object
    print("Pass" if rotated_array_search(None, 1) == -1 else "fail")