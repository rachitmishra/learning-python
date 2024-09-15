"""
Shell Sort

Approach: Divide and Conquer
Complexity:
Best case  -> O(nlogn)
Worst case -> O(n2)
"""


def swap(a, b, c):
    t = a  # a
    a = b  # b
    b = c  # c
    c = t


def sort_quick_partition(input_arr, i, j, p):
    if input_arr[i] > input_arr[p]:
        temp = input_arr[i]
        input_arr[i] = input_arr[j]
        input_arr[j] = input_arr[p]
        input_arr[p] = temp
        j -= 1
        p -= 1
    else:
        i += 1


def sort_quick(input_arr):
    print("""""""""""""""""""""""""")
    print("input " + str(input_arr))
    print("""""""""""""""""""""""""")

    le = len(input_arr)
    i = 0
    j = le - 2
    p = le - 1
    is_sorted = False
    while not is_sorted:
        if i == j:
            sort_quick_partition
            sort_quick_partition
        else:

        print("pass " + str(le - j - 1))
        print(str(input_arr))
        print("i => " + str(input_arr[i]) + " j => " + str(input_arr[j]) + " p => " + str(input_arr[p]))
        print("i -> " + str(i) + " j -> " + str(j) + " p -> " + str(p))
        print("\n")

        sort_quick_partition(input_arr, i, j, p)

    print("""""""""""""""""""""""""")
    print("result " + str(input_arr))
    print("""""""""""""""""""""""""")


if __name__ == '__main__':
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    sort_quick(arr)
