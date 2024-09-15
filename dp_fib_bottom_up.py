"""
Shell Sort

Approach: Divide and Conquer
Complexity: O(n3/2)
"""


def sort_shell(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    sublist_count = len(input_arr) // 2

    while sublist_count > 0:
        for start in range(sublist_count):
            step_sort_insertion(input_arr, start, sublist_count)

        print("pass " + str(start) + str(input_arr))
        sublist_count = sublist_count // 2

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


def step_sort_insertion(input_arr, start, step):
    for i in range(start + step, len(input_arr), step):
        current_value = input_arr[i]
        position = i

        while position >= step and input_arr[position - step] > current_value:
            input_arr[position] = input_arr[position - step]
            position = position - step

        input_arr[position] = current_value


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_shell(arr)
