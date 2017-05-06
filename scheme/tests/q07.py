test = {
  'names': [
    'q07',
    'q7',
    'Q7',
    '7'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> eval("(begin (+ 2 3) (+ 5 6))")
        4604790c89054dde998df1b491b0fa4b
        # locked
        >>> eval("(begin (define x 3) x)")
        0c31fd9672da616fabf24f1c95cc313f
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> eval("(begin 30 '(+ 2 2))")
        3ee6dd0237df9b6ccf29370a26873cc4
        # locked
        # choice: Pair('+', Pair(2, Pair(2, nil)))
        # choice: Pair('quote', Pair(Pair('+', Pair(2, Pair(2, nil))), nil))
        # choice: 4
        # choice: 30
        >>> eval('''
        ... (define x 0)
        ... (begin 42 (define x (+ x 1)))
        ... x
        ... ''')  # the last expression in do_begin_form should only be evaluated once
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> eval("(begin 30 'hello)")
        'hello'
        >>> eval("(begin (define x 3) (cons x '(y z)))")
        Pair(3, Pair('y', Pair('z', nil)))
        """,
        'type': 'doctest'
      }
    ]
  ]
}