"""
Insertion Sort

Approach: Loop
Complexity: O(n2)
"""


def sort_insertion(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    ln = len(input_arr)
    i = 1  # Assuming first element is sorted

    while i < ln:  # n times
        c = input_arr[i]
        p = i
        while p > 0 and input_arr[p - 1] > c:  # n times
            input_arr[p] = input_arr[p - 1]
            p -= 1
        input_arr[p] = c
        i += 1
        print("pass " + str(i) + " " + str(input_arr))

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_insertion(arr)
