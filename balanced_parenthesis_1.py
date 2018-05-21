# Assignment #3  Step#1  (Balanced Parenathesis)
# Yosh Kashima


# from Pattern import pattern
import doctest

Mystring = []
StackSize = 11


def DisplayStack():
    print("Stack currently contains:")
    for Item in Mystring:
        print (Item)


def Peek():
    if len(Mystring) > 0:
        print Mystring[-1]


def Push(Value):
    if len(Mystring) < StackSize:
        Mystring.append(Value)
    else:
        print ("Stack is full")


def Pop():
    if len(Mystring) > 0:
        return Mystring.pop()
    else:
        print("Stack is empty.")


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(Mystring):
    """
    A function to check balanced parenathesis.
    >>> is_paren_balanced("({[]})")
    True
    >>> is_paren_balanced("(){}[]([])")
    True
    >>> is_paren_balanced("[]{]")
    False
    >>> is_paren_balanced("([]}")
    False
    """
    if len(Mystring) < StackSize:
        is_paren_balanced = True
        index = 0

    while index < len(Mystring):

        paren = Mystring[index]

        if paren in "({[":
            Push(paren)

        else:

            top = Pop()

            if not is_match(top, paren):
                is_paren_balanced = False
        index += 1

    if len(Mystring) > 0 and is_paren_balanced:
        return True
    else:
        return False


def printing(string):
    print ("Given inputs    %s") % string


# def get_info():
#     user_input = raw_input("Given inputs:  ")
#     outcome = user_input
#     # print ("Returning String as Outcome %s" % outcome)
#     return outcome


if __name__ == "__main__":
    doctest.testmod

    printing("({[]})")
    print is_paren_balanced("({[]})")
    printing("(){}[]([])")
    print is_paren_balanced("(){}[]([])")
    printing("[]{]")
    print is_paren_balanced("[]{]")
    printing("([]}")
    print is_paren_balanced("([]}")
