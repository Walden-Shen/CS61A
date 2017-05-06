test = {
  'names': [
    'q02',
    'q2',
    'Q2',
    '2'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> read_line("(a . b)")
        8a7916d165b7a2050686f1cc78b1f536
        # locked
        # choice: Pair('a', Pair('b'))
        # choice: Pair('a', Pair('b', nil))
        # choice: SyntaxError
        # choice: Pair('a', 'b')
        # choice: Pair('a', 'b', nil)
        >>> read_line("(a b . c)")
        6f6acbac40c28f5fd4894bd1fa6afbdc
        # locked
        # choice: Pair('a', Pair('b', Pair('c', nil)))
        # choice: Pair('a', Pair('b', Pair('c')))
        # choice: Pair('a', 'b', 'c')
        # choice: Pair('a', Pair('b', 'c'))
        # choice: SyntaxError
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> read_line("(a b . c d)")
        7eb030ece2441dd5bb2c254cf41d086c
        # locked
        # choice: Pair('a', Pair('b', Pair('c', 'd')))
        # choice: Pair('a', Pair('b', 'c'))
        # choice: Pair('a', Pair('b', Pair('c', Pair('d', nil))))
        # choice: SyntaxError
        >>> read_line("(a . (b . (c . ())))")
        210d6521cd8b87ecabb8841b307f1889
        # locked
        # choice: Pair('a', Pair('b', Pair('c', nil)))
        # choice: SyntaxError
        # choice: Pair('a', Pair('b', Pair('c', Pair(nil, nil))))
        # choice: Pair('a', 'b', 'c')
        >>> read_line("(a . ((b . (c)))))")
        31dc52dac55247fa16755e288894dc5e
        # locked
        # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
        # choice: Pair('a', Pair('b', Pair('c', nil)), nil)
        # choice: Pair('a', Pair('b', Pair('c')), nil)
        # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil), nil)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> read_line("(. . 2)")
        SyntaxError
        >>> read_line("(2 . 3 4 . 5)")
        SyntaxError
        >>> read_line("(2 (3 . 4) 5)")
        Pair(2, Pair(Pair(3, 4), Pair(5, nil)))
        >>> read_line("(1 2")
        SyntaxError
        """,
        'type': 'doctest'
      }
    ]
  ]
}