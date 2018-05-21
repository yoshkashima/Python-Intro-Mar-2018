# import doctest


def print_line(row, n):
    """
    A function to print a row in pattern.

    >>> print_line(row=1, n=3)
    _ _ * _ _
    >>> print_line(row=2, n=3)
    _ * * * _
    >>> print_line(row=3, n=3)
    * * * * *
    """

    dash_count = n - row
    star_count = 2 * row - 1
    for i in range(dash_count):
        print "_",
    for i in range(star_count):
        print "*",
    for i in range(dash_count):
        print "_",


def pattern(n):
    """
    A function to print pattern based on input number.

    >>> pattern(n=1)
    *
    >>> pattern(n=2)
    _ * _
    * * *
    _ * _
    >>> pattern(n=3)
    _ _ * _ _
    _ * * * _
    * * * * *
    _ * * * _
    _ _ * _ _
    """
    for row in range(1, n + 1):
        print_line(row, n)
        print

    for row in range(n - 1, 0, -1):
        print_line(row, n)
        print


if __name__ == "__main__":
    # doctest.testmod()
    pattern(3)
