test = {
  'names': [
    'q05A',
    'q5A',
    'Q5A',
    'qA5',
    'QA5',
    'A5',
    '5A',
    '5'
  ],
  'points': 1,
  'suites': [
    [
      {
        'answer': '4603abca9e6c9956574a67ffb7be2487',
        'choices': [
          r"""
          Pair(A, Pair(B, nil)), where:
          A is the symbol being bound,
          B is an expression whose value should be bound to A
          """,
          r"""
          Pair(A, Pair(B, nil)), where:
            A is the symbol being bound,
            B is the value that should be bound to A
          """,
          r"""
          Pair(A, B), where:
            A is the symbol being bound,
            B is the value that should be bound to A
          """,
          r"""
          Pair(A, B), where:
            A is the symbol being bound,
            B is an expression whose value should be bound to A
          """,
          r"""
          Pair('define', Pair(A, Pair(B, nil))), where:
            A is the symbol being bound,
            B is an expression whose value should be bound to A
          """
        ],
        'locked': True,
        'question': 'What is the structure of the argument vals?',
        'type': 'concept'
      },
      {
        'answer': 'b776d636d5ff3f2a7a941f90838c83de',
        'choices': [
          'make_call_frame',
          'define',
          'lookup',
          'bindings'
        ],
        'locked': True,
        'question': r"""
        What method of a Frame instance will bind
        a value to a symbol in that frame?
        """,
        'type': 'concept'
      },
      {
        'locked': True,
        'test': r"""
        >>> eval('''
        ...   (define size 2)
        ...   size
        ... ''')
        f0c1f6d92f853abf152683e4827fb490
        # locked
        # choice: 'size'
        # choice: None
        # choice: SchemeError
        # choice: 2
        >>> eval('''
        ...   (define x (+ 2 3))
        ...   x
        ... ''')
        4c165dab3afb51604895132221bf0eb7
        # locked
        # choice: Pair('+', Pair(2, Pair(3, nil)))
        # choice: 5
        # choice: SchemeError
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> eval("(define size 2)")   # do_define_form should return the target
        'size'
        >>> eval('''
        ... (define pi 3.14159)
        ... (define radius 10)
        ... (* pi (* radius radius))
        ... ''')
        314.159
        >>> eval("(define 0 1)")
        SchemeError
        """,
        'type': 'doctest'
      }
    ]
  ]
}