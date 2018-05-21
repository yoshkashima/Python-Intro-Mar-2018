# Assignment 04 - Balanced Paranthesis using Object oriented programming
# Yosh Kashima
# Date 5/16/2018

import doctest


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()   # method

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def get_len(self):
        return len(self.items)

    def print_rpr(self):
        newstring = str(self.items).strip('[]')
        showstring_no_quotes = newstring.replace("'", "")
        showstring_no_comma = showstring_no_quotes.replace(",", "")
        showstring = showstring_no_comma
        return ('Stack:  %s' % showstring)


def printing(string):
    print ("My stack is as the follows:  %s") % string


def get_info():
    user_input = raw_input("Given inputs    ")
    outcome = user_input
    # print ("Returning String as Outcome %s" % outcome)
    return outcome


def clear():
    global stack
    stack = []
# write remaining methods here


MAPPING = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_balanced(input_string):
    """
    Return True if all paraentheses are balanced, otherwise return False.

    >>> is_balanced("({})")
    True

    >>> is_balanced("({}[[]])")
    True

    >>> is_balanced("([]}")
    False

    >>> is_balanced("(((()")
    False

    >>> is_balanced("}")
    False

    >>> is_balanced("")
    True

    """
    clear()
    stack = Stack()
    for item in input_string:
        if item in MAPPING.values():
            stack.push(item)
            # print (stack.get_stack())
        else:
            if stack.is_empty():
                return False
            value = stack.pop()
            # print (stack.get_stack())
            # print (value)
            if value != MAPPING[item]:
                return False

    if not stack.is_empty():
        return False
    return True


if __name__ == "__main__":
    doctest.testmod()
    stack = Stack()
    print (stack.is_empty())
    stack.push("{")
    stack.pop()
    stack.push("[")
    stack.push("{")
    stack.push("(")
    print (stack.get_len())
    stack.pop()
    print (stack.get_len())
    print (stack.get_stack())
    stack.push("(")
    print (stack.get_stack())
    print ('My stack is follows: %s' % stack.print_rpr())
    print is_balanced("({})")
    print is_balanced("({}[[]])")
    print is_balanced("([]}")
    print is_balanced("(((()")
    print is_balanced("}")
    print is_balanced("")
