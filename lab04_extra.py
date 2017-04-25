from lab04 import *

# Q9
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    answer = []
    while lst:
        answer.append(lst.pop())
    return answer

# Q10
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) < 2:
        return seq
    else:
        return merge(mergesort(seq[:len(seq) // 2]), mergesort(seq[len(seq) //
            2:]))

#teacher's iteration version --- really nb
def mergesort_iter(seq):
    if not seq:
        return seq
    queue = [[elem] for elem in seq]
    while len(queue) > 1:
        first, second = queue[0], queue[1]
        queue = queue[2:] + [merge(first, second)]
    return queue[0]
            
# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if lower <= fn(x) <= upper]

# Q12
def deck(suits, numbers):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and numbers. Each element in the returned list should be of the form
    [suit, number].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    return [[x, y] for x in suits for y in numbers]

# Q13
def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in
            range(len(x))]


