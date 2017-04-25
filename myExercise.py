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
    print(n // pow(10, length - 1))

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
        fib_n = root(left) +root(right)
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
    temproot = pow(root(tree), 2)
    if branches(tree):
        return [temproot] + [square_tree(branch) for branch in branches(tree)]
    else:
        return [temproot]

#return the height of a Tree
def height(tree):
    if is_leaf(tree):
        return
    else:
        return max([branch + 1 for branch in branches(tree)])

#return the number of nodes
def tree_size(tree):
    if is_leaf(tree):
        return 1
    else:
        return 1 + tree_size(branches(tree))


"""
8. Function vary in different environment
"""
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print('insufficient balance')
            return
        balance = balance - amount
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
