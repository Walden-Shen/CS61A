def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert upper_bound(y) < 0 or lower_bound(y) > 0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    return interval(lower_bound(x) - upper_bound(y), upper_bound(x) -
            lower_bound(y))

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
#r1: (4, 8) r2: (1, 3)

def multiple_references_explanation():
    return """The mulitple reference problem..."""
#because each time a variable appears, it widens the bound of the interval.So
#unnecessary same variable is bad

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    extremepoint = -b / (2 * a)
    if lower_bound(x) < extremepoint < upper_bound(x):
        if a > 0:
            return interval(a * pow(extremepoint, 2) + b * extremepoint + c,
                    max((a * pow(lower_bound(x), 2) + b * lower_bound(x) + c),
                        (a * pow(upper_bound(x), 2) + b * upper_bound(x) + c)))
        else:
            return interval(min((a * pow(lower_bound(x), 2) + b * lower_bound(x) + c),
                        (a * pow(upper_bound(x), 2) + b * upper_bound(x) + c)),
                        a * pow(extremepoint, 2) + b * extremepoint + c)
    else:
        return interval(min((a * pow(lower_bound(x), 2) + b * lower_bound(x) + c),
                    (a * pow(upper_bound(x), 2) + b * upper_bound(x) + c)),
                max((a * pow(lower_bound(x), 2) + b * lower_bound(x) + c),
                    (a * pow(upper_bound(x), 2) + b * upper_bound(x) + c)))


def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    poly = len(c)
    def polyfunction(x):
        i = 0
        answer = 0
        while i < poly:
            answer += c[poly - i - 1] * pow(x, poly - i - 1)
            i += 1
        return answer





