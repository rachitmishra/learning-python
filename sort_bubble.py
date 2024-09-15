"""
Bubble Sort

Approach: Loop
Complexity: O(n2)
"""


def sort_bubble(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    length = len(input_arr)
    i = 0  # first element
    while i < (length - 1):  # n times
        print("pass " + str(i) + " " + str(input_arr))
        j = i
        while j < (length - 1):
            if input_arr[j] > input_arr[j + 1]:
                temp = input_arr[j]
                input_arr[j] = input_arr[j + 1]
                input_arr[j + 1] = temp
            j += 1
        i += 1

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_bubble(arr)
