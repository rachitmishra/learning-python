"""
Dynamic programming: Memoized

Fibonacci
"""


def dp_fib(n):
    if n <= 2:
        return 1
    else:
        return dp_fib(n - 1) + dp_fib(n - 2)


if __name__ == '__main__':
    num = 9
    print("""""""""""""""""""""""""")
    print("input " + str(num))
    print("""""""""""""""""""""""""")

    result = dp_fib(num)

    print("""""""""""""""""""""""""")
    print("result " + str(result))
    print("""""""""""""""""""""""""")