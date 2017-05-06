test = {
  'names': [
    'q14B',
    'Q14B',
    'qB14',
    'QB14',
    'B14',
    '14B',
    '14'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> eval("(and)")
        f34008a6e4d61f073f26ac75528dcec4
        # locked
        # choice: True
        # choice: False
        # choice: SchemeError
        >>> eval("(and 1 #f)")
        4b73e7938f0746cf953fe05cb617337f
        # locked
        # choice: 1
        # choice: True
        # choice: False
        >>> eval("(and 2 1)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        # choice: 2
        # choice: 1
        # choice: True
        # choice: False
        >>> eval("(and #f 5)")
        4b73e7938f0746cf953fe05cb617337f
        # locked
        # choice: 5
        # choice: True
        # choice: False
        >>> eval('''
        ... (define x 0)
        ... (and 3 (define x (+ x 1)))
        ... x
        ... ''')
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval('''
        ... (define x 0)
        ... (and (begin (define x (+ x 1)) #f) 3)
        ... x
        ... ''')
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> eval("(and 3 2 #f)")
        False
        >>> eval("(and 3 2 1)")
        1
        >>> eval("(and 3 #f 5)")
        False
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> eval("(or)")
        4b73e7938f0746cf953fe05cb617337f
        # locked
        # choice: True
        # choice: False
        # choice: SchemeError
        >>> eval("(or 1)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        # choice: 1
        # choice: True
        # choice: False
        # choice: SchemeError
        >>> eval("(or #f)")
        4b73e7938f0746cf953fe05cb617337f
        # locked
        # choice: True
        # choice: False
        # choice: SchemeError
        >>> eval("(or 0 1 2 'a)")
        be98a0e00bbf18e70dc9c837ba5c109f
        # locked
        >>> eval('''
        ... (define x 0)
        ... (or (define x (+ x 1)) 3)
        ... x
        ... ''')
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval('''
        ... (define x 0)
        ... (or #f (define x (+ x 1)))
        ... x
        ... ''')
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> eval("(or #f #f)")
        False
        >>> eval("(or 'a #f)")
        'a'
        >>> eval("(or (< 2 3) (> 2 3) 2 'a)")
        True
        >>> eval("(or (< 2 3) 2)")
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}