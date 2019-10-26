def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        return None

    if number < 2:
        return number

    low = 2
    high = number//2

    while low <= high:
        mid = (low+high)//2
        if mid**2 > number:
            high = mid - 1
        elif mid**2 < number:
            low = mid + 1
        else:
            # if mid**2 == number
            return mid
    # Otherwise return the high number
    return high


if __name__ == '__main__':
    # Default test cases
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")

    # Round to the nearest int square root
    print("Pass" if (3 == sqrt(10)) else "Fail")
    print("Pass" if (100 == sqrt(10011)) else "Fail")

    # Handing large numbers
    print("Pass" if (777 == sqrt(603729)) else "Fail")

    # Handling non-int input
    print("Pass" if (None == sqrt(None)) else "Fail")