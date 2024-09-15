"""
Binary search

Slicing is O(k)
Complexity: O(log(n))
"""


def search_binary(input_array, value):
    low = 0
    high = len(input_array) - 1
    le = len(input_array)

    if le == 0:
        return False
    else:
        mid = (low + high) // 2
        if input_array[mid] == value:
            return True
        elif input_array[mid] > value:
            return search_binary(input_array[low: mid], value)
        elif input_array[mid] < value:
            return search_binary(input_array[mid + 1:], value)

    return -1


if __name__ == '__main__':
    test_list = [1, 3, 9, 11, 15, 19, 29, 31]
    test_val1 = 25
    test_val2 = 15
    test_val3 = 31
    print (search_binary(test_list, test_val1))
    print (search_binary(test_list, test_val2))
    print (search_binary(test_list, test_val3))
