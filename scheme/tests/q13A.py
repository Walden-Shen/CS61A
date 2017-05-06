test = {
  'names': [
    'q13A',
    'Q13A',
    'qA13',
    'QA13',
    'A13',
    '13A',
    '13'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> eval("(if #t 1 0)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if #f 1 0)")
        be98a0e00bbf18e70dc9c837ba5c109f
        # locked
        >>> eval("(if 1 1 0)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if 0 1 0)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if 'a 1 0)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if (cons 1 2) 1 0)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if #t 1)")
        3fff5f136c823d9cefa95b502d20b1e3
        # locked
        >>> eval("(if #f 1)")
        15d809dd1a8d1d347add316cff2e95bf
        # locked
        >>> eval("(if #t '(1))")
        ad6118f4c42efea3550065b823719ceb
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}