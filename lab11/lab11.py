#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start
        self.now = start
        self.end = end

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.now > self.end:
            raise StopIteration
        self.now += 1
        return self.now - 1
        

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        self.now = self.start
        return self

##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
        yield n
        n -= 1

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, n):
        self.count = n


    def __iter__(self):
        while self.count >= 0:
            yield self.count
            self.count -= 1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield (int)(n)
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n /= 2
        yield (int)(n)
