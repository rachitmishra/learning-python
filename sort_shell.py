"""
Shell Sort

Approach: Divide and Conquer
Complexity: O(n3/2)
"""


def sort_shell(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    ln = len(input_arr)
    step = 3
    i = 0
    while step > 0:
        while i < ln:  # n times
            c = input_arr[i]
            p = i

            while p > 0 and input_arr[p - step] > c:  # n times
                input_arr[p] = input_arr[p - step]
                p -= step
            input_arr[p] = c
            i += step
            print("pass " + str(i) + " " + str(input_arr))
        step -= 1

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_shell(arr)
