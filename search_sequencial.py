"""
Sequential search

Complexity O(n)
"""


def search_sequential(input_array, value):
    i = 0
    le = len(input_array)
    while i < le - 1:
        if input_array[i] == value:
            return True
        else:
            i += 1


if __name__ == '__main__':
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    print search_sequential(test_list, test_val1)
    print search_sequential(test_list, test_val2)
