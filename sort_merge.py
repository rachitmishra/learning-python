"""
Merge Sort

Approach: Divide and Conquer
Complexity: O(nlogn)
"""


def sort_merge(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    if len(input_arr) > 1:
        mid = len(input_arr) // 2
        left_half = input_arr[:mid]
        right_half = input_arr[mid:]

        sort_merge(left_half)
        sort_merge(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_arr[k] = left_half[i]
                i += 1
            else:
                input_arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            input_arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_arr[k] = right_half[j]
            j += 1
            k += 1

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_merge(arr)
