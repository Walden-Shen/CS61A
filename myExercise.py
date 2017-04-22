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
