"""
Stack

Base converter
"""
from ds_stack import Stack


def base_converter(number, base):
    digits = "0123456789ABCDEF"

    s = Stack()

    while number > 0:
        r = number % base
        s.push(r)
        number = number // base

    result = ""
    while not s.is_empty():
        result = result + digits[s.pop()]

    return result


if __name__ == '__main__':
    print(base_converter(25, 2))
    print(base_converter(25, 16))
    print(base_converter(256, 16))
    print(base_converter(26, 26))
    print(base_converter(25, 8))
