test = {
  'names': [
    'q01',
    'q1',
    'Q1',
    '1'
  ],
  'points': 1,
  'suites': [
    [
      {
        'never_lock': True,
        'test': r"""
        >>> read_line('3')
        3
        >>> read_line('-123')
        -123
        >>> read_line('1.25')
        1.25
        >>> read_line('true')
        True
        >>> read_line('(a)')
        Pair('a', nil)
        >>> read_line(')')
        SyntaxError
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> read_line("'x")
        39fe81be80f506d555ca9800d1d78f9d
        # locked
        # choice: Pair('x', nil)
        # choice: 'x'
        # choice: Pair('quote', 'x')
        # choice: Pair('quote', Pair('x', nil))
        >>> read_line("(quote x)")
        39fe81be80f506d555ca9800d1d78f9d
        # locked
        # choice: Pair('quote', 'x')
        # choice: Pair('x', nil)
        # choice: 'x'
        # choice: Pair('quote', Pair('x', nil))
        >>> read_line("'(a b)")
        0b8ff81c0ca764b4f0fbf5ac57b27c84
        # locked
        # choice: Pair('a', Pair('b', nil))
        # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
        # choice: Pair('quote', Pair('a', 'b'))
        # choice: Pair('quote', Pair('a', Pair('b', nil)))
        >>> read_line("'((a))")
        06c0a00e3a7367a6e3df2414156d09cc
        # locked
        # choice: Pair('quote', Pair(Pair('a', nil), nil))
        # choice: Pair('quote', Pair(Pair('a', nil), nil), nil)
        # choice: Pair('quote', Pair(Pair('a'), nil))
        # choice: Pair('quote', Pair(Pair('a'), nil), nil)
        # choice: Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> read_line("(a (b 'c))")
        Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair('c', nil)), nil)), nil))
        >>> read_line("(a (b '(c d)))")
        Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair(Pair('c', Pair('d', nil)), nil)), nil)), nil))
        >>> read_line("')")
        SyntaxError
        """,
        'type': 'doctest'
      }
    ]
  ]
}