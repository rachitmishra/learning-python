"""
Stack

Parenthesis checker
"""
from ds_stack import Stack


def par_checker(symbol_str):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbol_str):
        if symbol_str[i] in "([{":
            s.push(symbol_str[i])
        else:
            if s.is_empty():
                balanced = False
            else:
                if s.reverse_peak(i) == s.peak_pos(i):
                    s.pop()
                else:
                    balanced = False

        i += 1

    if balanced and s.is_empty():
        return True

    return False


if __name__ == '__main__':
    print(par_checker('((()))'))
    print(par_checker('([())]'))
