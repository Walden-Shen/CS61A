"""
1.using function as argument
"""
def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    assert n > 0, "n should be more than 0"
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

"""
2.return a function && doctest
"""
def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def func(x):
        return x + n
    return func

"""
3.my recursion and the recursion of teacher's containing lambda
"""

def inverseCascade(n):
    cnt, temp = 0, n
    while(temp > 0):
        cnt += 1
        temp //= 10
    ancillaryInverseCascade(n, cnt)

def ancillaryInverseCascade(n, length):
    print(n // pow(10, length - 1))
    if length > 1:
        ancillaryInverseCascade(n, length - 1)
    else:
        return

"teacher's version"
def inverse_Cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n : f_then_g(print, shrink, n//10)


"""
4.a new recursion exercise : my version
"""
def countPartitions(targetSum, largestNumber):
    assert targetSum > 0, "the first argument should be more than 1"
    if(largestNumber == 0 or targetSum == 0):
        return 0
    elif(largestNumber <= targetSum):
        if(targetSum - largestNumber > 0):
            return countPartitions(targetSum, largestNumber - 1) + countPartitions(targetSum - largestNumber, largestNumber)  
        else:
            return countPartitions(targetSum, largestNumber - 1) + 1
    return countPartitions(targetSum, largestNumber - 1)

"teacher's version"
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)

"""
5.GCD and function descriptor
"""
def gcd(m, n):
    if m % n == 0:
        return n
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m - n, n)

def trace(f):
    def traced(m, n):
        print('Called on ', m, 'and', n)
        return f(m, n)
    return traced
"""
6.silly handout concerning recursion
"""
def expt(base, power):
    """
    >>> expt(2, 3)
    8
    >>> expt(2, -1)
    0.5
    """
    if power == 1:
        return base
    elif power == 0:
        return 1
    elif power > 1:
        return expt(base, power - 1) * base
    else:
        return expt(base, power + 1) / base

def count_stair_ways(n):
    if n >= 1:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2) 
    elif n == 0:
        return 1
    else:
        return 0

def pascal(row, column):
    if column == 0:
        return 1
    elif column == row:
        return 1
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)

def has_sum(sum, n1, n2):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5)
    True
    """
    if sum < 0:
        return False
    elif sum % n1 == 0 or sum % n2 == 0:
        return True
    else:
        return has_sum(sum - n1, n1, n2) or has_sum(sum - n2, n1, n2)

"""
7. Tree
"""
def tree(root, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
         return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

#create a fib tree
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        counts = [count_leaves(b) for b in branches(tree)]
        return sum(counts)

#present all the leaves of this tree
def leaves(tree):
    if is_leaf(tree):
        return [root(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

#part the number n with numbers lower or equal to m
def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])

#function with the previous function
def print_parts(tree, partition = []):
    if is_leaf(tree):
        if root(tree):
            print(partition)
    else:
        left, right = branches(tree)
        print_parts(left, partition + [root(tree)])
        print_parts(right, partition)

#square every item in the tree
def square_tree(tree):
    temproot = (int)(pow(root(tree), 2))
    if branches(tree):
        return [temproot] + [square_tree(branch) for branch in branches(tree)]
    else:
        return [temproot]

#return the height of a Tree
def height(tree):
    if is_leaf(tree):
        return 1
    else:
        return max([height(branch) + 1 for branch in branches(tree)])

#return the number of nodes
def tree_size(tree):
    if is_leaf(tree):
        return 1
    else:
        return 1 + sum([tree_size(branch) for branch in branches(tree)])

#return the max number in the Tree
def tree_max(tree):
    if is_leaf(tree):
        return root(tree)
    else:
        return max([root(tree)] + [tree_max(branch) for branch in
            branches(tree)])

#expression Tree
from operator import add, mul
def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree(mul, [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree(add, [expr, tree(4)]))
    10
    """
    if not is_leaf(tree):
        return root(tree)(eval_tree(tree[1]), eval_tree(tree[2]))
    else:
        return root(tree)

#hailstone tree
def hailstone_tree(n, height):
    """Generates a tree of hailstone numbers that will reach N
    , with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if height == 0:
        return [n]
    elif (float)((n - 1) / 3) == (int)((n - 1) // 3) and (n - 1) // 3 % 2 == 1 and (n - 1) // 3 != 1:
        return [n] + [hailstone_tree(2 * n, height - 1)] + [hailstone_tree((n -
            1) // 3, height - 1)]
    else:
        return [n] + [hailstone_tree(2 * n, height - 1)]
#find path in a tree assuming all the value in the tree is unique
def find_path(tree, x):
    """ Return a path in a tree to a leaf with value X,
    None if such a leaf is not present.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 6)
    [2, 7, 6]
    >>> find_path(t, 10)
    """
    global temp
    if root(tree) == x:
        temp = []
        return True
    elif is_leaf(tree):
        return False
    else:
        for branch in branches(tree):
            if find_path(branch, x):
                temp = [root(branch)] + temp
                return [root(tree)] + temp

"""
8. Function vary in different environment
"""
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print('insufficient balance')
            return
        balance -= amount
        return balance
    return withdraw

"""
9. OOP 2.25
"""
class Account:
    interest = 0.02 
    # using Account.interest = n can change all the objects'
    # interest. Else if you change one object's interest , only its interest is
    # changed
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

class CheckingAccount(Account):
    """
    Inheritance
    """
    interest = 0.01 #overriding
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    #designing for Inheritance
    #1. dont repeat yourself. using existing implementations. 2.reuse overridden
    #attributes by accessing through the base class 3. look up attributes on
    #instances if possible

class BestAccount(CheckingAccount, Account):
    deposit_fee = 2
    
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
    
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class Bank:
    def __init__(self):
        self.accounts = [] # composition
    
    def open_account(self, holder, amount, account_type = CheckingAccount):
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)

"""
10. Discussion 5: Mutable data and nonlocal (this section of problems are too
simple to put on this file, shame)
"""
#lst.insert(i, value)  lst.sort()

def reverse_list(lst):
    """Reverses lst in-place (mutating the original list).
    >>> lst = [1, 2, 3, 4]
    >>> reverse_list(lst)
    >>> lst
    [4, 3, 2, 1]
    >>> pi = [3, 1, 4, 1, 5]
    >>> reverse_list(pi)
    >>> pi
    [5, 1, 4, 1, 3]
    """
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]


def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 3, 3: 4}, 2: {4: 4, 5: 3}}
    >>> replace_all_deep(d, 3, 1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """
    for key, value in d.items():
        if type(value) == int:
            if value == x:
                d[key] = y
        else:
            replace_all_deep(value, x, y)

"""
11. lecture on 15.3.2
"""
#the difference between repr(foo) && str(foo) is that the first one illustrates
#the python version of foo while the str illustrates humanreadable version. for
#example : import datetime; today = datetime.date(2020,1,1); repr(today) =
#'datetime.date(2020,1,1)' while str(today) is '2020-1-1'. Whats more, when you
#use the eval function to the str(today) && repr(today), you will find that
#error arises when eval(str(today)) since that's human version

#and the amazing part of str && repr is that they are polymorphic function,
#which applies to all the functions. Because they dont deal with their argument
#but to ask the object to call __repr__() or __str__() which are all built in
#functions of all the objects.
class Bear:
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'oski the bear' 

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    """
    >>> print_bear()
    a bear 
    a bear 
    Bear()
    oski
    oski the bear 
    """
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__repr__())
    print(oski.__str__())
#the behavior of repr: 1. An instance attribute called __repr__ is ignored
#the behavior of str: 1. An instance attribute called __str__ is ignored. 2. If
#no __str__ attribute is found, uses repr string.

def repr(o):
    return type(o).__repr__(o)

def str(o):
    if hasattr(type(o), '__str__'):
        return type(o).__str__(o)
    else:
        return repr(o)

"""
12. Complex number system
"""
#property decorator: designates that it will be called whenever it is looked up
#on an instance. It unifies the representation of different forms
from math import *
class Number:
    """
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)
    """

#you can also coerce the rational to ComplexRI cuz rational is a ComplexRI
#without imaginary
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)
    
    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))

    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)

    def rational_to_complex(r):
        return ComplexRI(r.numer / r.denom, 0)

    coercions = {('rat', 'com'): rational_to_complex}
    """
    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    def __mul__(self, other):
        return self.mul(other)

    def add_complex_and_rational(c, r):
        return ComplexRI(c.real + r.numer / r.denom, c.imag)

    def add_rational_and_complex(c, r):
        return ComplexRI(c.numer / c.denom + r.real, r.imag)
    
    adders = {("com", "rat"): add_complex_and_rational, ("rat", "com"): add_rational_and_complex}
    """
class Rational(Number):
    type_tag = "rat"
    def __init__(self, n, d):
        g = gcd(n, d)
        self.numer = n // g
        self.denom = d // g
    
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    @property
    def float_value(self):
        return self.numer / self.denom

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)
class Complex(Number):
    type_tag = "com"
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)
    
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle
                / pi)
"""
13. Linked List
"""
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)
"""
13.memoized
"""
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted
#I make a lot of effort to figure this memo why it is recursive: cuz when you
#call fib = memo(fib), the reference to f is also changed. Then it is recursive
def memo(f):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)#*args break the tuple args into many arguments
            print(cache[args])
        return cache[args]#args is a tuple
    return memoized

"""
14.Tree Class
"""
class Tree:
    def __init__(self, entry, branches = ()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree) #inherit from Tree is also ok
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_repr = ", " + repr(self.branches)
        else:
            branches_repr = ""
        return "Tree({0}{1})".format(self.entry, branches_repr)
@memo
def fib_treeclass(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left, right = fib_treeclass(n - 2), fib_treeclass(n - 1)
        return Tree(left.entry + right.entry, [left, right])

#a function helps me to figure out how many frames exist
def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.max_count < counted.open_count:
            counted.max_count = counted.open_count
        result = f(n)
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t # Assuming __repr__ is defined
    Tree(2, [Tree(2, [Tree(4)]), Tree(4), Tree(6)])
    """
    if t.entry % 2:
        t.entry = t.entry + 1
    for branch in t.branches:
        make_even(branch)

def average_tree(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> average_tree(t)
    3
    """
"""
15.iterator
"""
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return max(self.end - self.start, 0)

    def __getitem__(self, k):
        if self.start + k >= self.end:
            raise IndexError
        return self.start + k

class RangeIter:
    def __init__(self, start, end):
        self.next = start
        self.end = end
    
    def __next__(self):
        if self.next >= self.end:
            raise StopIteration
        result = self.next
        self.next += 1
        return result
class Letters:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return LetterIter(self.start, self.ent)

class LetterIter:
    def __init__(self, start, end):
        self.next_letter = start
        self.end = end
    
    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration
        result = self.next_letter
        self.next_letter = chr(ord(self.next_letter) + 1)
        return result
    
def letter_generator(next_letter, end):
    while next_letter < end:
        yield next_letter
        next_letter = chr(ord(next_letter) + 1)
#the map (built in function) is lazy.'map(function, iterable things)', you would
#receive a map object and only next(that object) can cast the function to the
#iterable thing. BTW list(that object) can list all the things after the function

