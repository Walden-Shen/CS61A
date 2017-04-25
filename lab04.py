# Q5
def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    return(ancillary(lst, []))

def ancillary(lst, answer):
    if len(lst) > 0:
        answer.append(lst.pop())
        return ancillary(lst, answer) #here must exists an return. or the answer
   # will be in other locations
    else:
        return answer

#teacher's version
def teacher(lst):
    if not lst:
        return []
    return teacher(lst[1:]) + [lst[0]]


# Q6
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif lst1[0] >= lst2[0]:
        return merge([lst2[0]] + lst1, lst2[1:])
    else:
        i = 0
        for elements in lst1:
            if lst2[0] < elements:
                return merge(lst1[:i] + [lst2[0]] + lst1[i:], lst2[1:])    
                break
            i += 1
        return merge(lst1[:i] + [lst2[0]], lst2[1:])
#teacher's version
def mergeteacher(lst1, lst2):
    if not lst1 or lst2:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge[lst1[1:], lst2]
    else:
        return [lst2[0]] + merge[lst1, lst2[1:]]

# Q8
from math import sqrt

def is_square(n):
    return float(sqrt(n)) == int(sqrt(n))

def squares(seq):
    """Returns a new list containing elements of the original list that are
    perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> squares(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [elements for elements in seq if is_square(elements)]

