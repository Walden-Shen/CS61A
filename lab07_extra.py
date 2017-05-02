## Extra Recursive Objects ##

from lab07 import *

# Linked List Practice

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> list_to_link([1, 2, 3])
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"
    if lst:
        return Link(lst[0], list_to_link(lst[1:]))
    else:
        return Link.empty

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> reverse(Link(1))
    Link(1)
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> link
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"
    new = Link(link.first)
    while link.rest is not Link.empty:
        link = link.rest
        new = Link(link.first, new)
    return new

def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"
    """unable to finish
    if link.rest is not Link.empty:
        previous = link
        this = mutate_reverse(link.rest)
        temp = this
        while temp.rest is not Link.empty:
            temp = temp.rest
        temp.rest = Link(previous.first)
        return this
    else:
        return link
    """
    if link is Link.empty or link.rest is Link.empty:
        return
    mutate_reverse(link.rest)
    while link.rest is not Link.empty:
        link.first, link.rest.first = link.rest.first, link.first
        link = link.rest


# Tree Practice

def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return [t.entry]
    else:
        answer = []
        for branch in t.branches:
            answer += leaves(branch)
        return answer

def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return Tree(t.entry)
    else:
        entry = t.entry
        for branch in t.branches:
            entry += cumulative_sum(branch).entry
        return Tree(entry, [cumulative_sum(branch) for branch in t.branches])
    #standard answer. the internal thought is identical however is more elegant than me
    """
    branches = [cumulative_sum(st) for st in t.branches]
    new_entry = sum(st.entry for st in branches) + t.entry
    return Tree(new_entry, branches)
    """
    #I made a mutable version by mistake
    """
    if t.is_leaf():
        return t.entry
    else:
        for branch in t.branches:
            t.entry += cumulative_sum(branch)
    """


def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = cumulative_sum(t)
    >>> same_shape(t, s)
    True
    """
    "*** YOUR CODE HERE ***"
    if len(t1.branches) == len(t2.branches):
        answer = True
        for i in range(len(t1.branches)):
            answer &= same_shape(t1.branches[i], t2.branches[i])
        return answer
    return False
#standard answer: return len(t1.branches) == len(t2.branches) and
#all(same_shape(st1, st2) for st1, st2 in zip(t1.branches, t2.branches))


# Folding Linked Lists

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn, fn(z, link.first))

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
        return lambda a: g(fn(a, x))
    return foldr(link, step, identity)(z)
