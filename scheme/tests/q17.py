test = {
  'names': [
    'q17',
    'Q17',
    '17'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> eval('''
        ... (define f (mu (x) (+ x y)))
        ... (define g (lambda (x y) (f (+ x x))))
        ... (g 3 7)
        ... ''')
        9ac6645b528a5e548dbf91b465c17717
        # locked
        >>> eval('''
        ... (define g (mu () x))
        ... (define (high f x)
        ...   (f))
        ... (high g 2)
        ... ''')
        f0c1f6d92f853abf152683e4827fb490
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> eval('''
        ... (define (f x) (mu () (lambda (y) (+ x y))))
        ... (define (g x) (((f (+ x 1))) (+ x 2)))
        ... (g 3)
        ... ''')
        4140f2142c26074c7b4062d07b212f51
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}