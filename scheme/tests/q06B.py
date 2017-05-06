test = {
  'names': [
    'q06B',
    'q6B',
    'Q6B',
    'qB6',
    'QB6',
    'B6',
    '6B',
    '6'
  ],
  'points': 1,
  'suites': [
    [
      {
        'answer': '86b850b899641ec908153870884e9153',
        'choices': [
          r"""
          Pair('quote', Pair(A, nil)), where:
            A is the quoted expression
          """,
          r"""
          [A], where:
            A is the quoted expression
          """,
          r"""
          Pair(A, nil), where:
            A is the quoted expression
          """
        ],
        'locked': True,
        'question': 'What does the parameter vals look like?',
        'type': 'concept'
      },
      {
        'locked': True,
        'test': r"""
        >>> eval("(quote 3)")
        0c31fd9672da616fabf24f1c95cc313f
        # locked
        # choice: Pair('quote', Pair(3, nil))
        # choice: Pair(3, nil)
        # choice: 3
        >>> eval("(quote (1 2))")
        08d24f564232ffc9d2cf881400e7a329
        # locked
        # choice: Pair('quote', Pair(1, Pair(2, nil)))
        # choice: Pair(1, 2)
        # choice: Pair(1, Pair(2, nil))
        # choice: SchemeError
        >>> eval("(car '(1 2 3))")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(car (car '((1))))")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("'hello")
        d98bb0b8b49acb7f9b557e54fdc370bd
        # locked
        # choice: Pair('quote', Pair('hello', nil))
        # choice: Pair('hello', nil)
        # choice: 'hello'
        >>> eval("''hello")
        831d1d13d0f6fd722df190f152537a18
        # locked
        # choice: Pair('quote', Pair('quote', Pair('hello', nil)))
        # choice: Pair('quote', Pair('hello', nil))
        # choice: Pair('hello', nil)
        # choice: 'hello'
        """,
        'type': 'doctest'
      }
    ]
  ]
}