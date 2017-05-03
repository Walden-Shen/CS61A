## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"
    temp = set(lst)
    for s in temp:
        if n - s in temp and n - s is not s:
            return True
    return False

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"
    if k == 1:
        return n
    elif k % 2:
        return n * pow(n, k - 1)
    else:
        return pow(n, k // 2) ** 2

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst) + 1):
        if i not in lst:
            return i
    # return sum(range(max(lst) + 1)) - sum(lst)
        
def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    "*** YOUR CODE HERE ***"
    lst = lst[:k + 1]
    return find_duplicates(lst)

def find_duplicates_k_l(k, l, lst):
    """Returns True if there are any two values who in lst that are within k
    indices apart AND if the absolute value of their difference is less than
    or equal to l.
    >>> find_duplicates_k_l(1, 100, [100, 23, 199, 275, 320, 988, 27])
    True
    """
    lst = lst[:k + 1]
    lst.sort()
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) <= l:
            return True
    return False
