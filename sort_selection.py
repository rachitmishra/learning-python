"""
Selection Sort

Approach: Loop
Complexity: O(n2)
"""


def selection_sort(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    i = 0
    ln = len(input_arr)
    while i < ln:  # n times
        m = i
        j = i + 1
        while j < ln:  # n times
            if input_arr[j] < input_arr[m]:
                m = j
            j += 1
        temp = input_arr[i]
        input_arr[i] = input_arr[m]
        input_arr[m] = temp
        i += 1
        print("pass " + str(i) + str(input_arr))

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    selection_sort(arr)
