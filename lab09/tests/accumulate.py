test = {
  'name': 'accumulate',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate + 0 4 square)
          15652c8e697e11e5d9522f9191c2cb45
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (accumulate * 3 5 id)
          43fd85c2b715943e3b6457454aeeaa09
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (accumulate + 0 3 add-one)
          24501e5e22e5149e7702cb00bdfc079c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09-extra)
      scm> (define (square x) (* x x))
      scm> (define (id x) x)
      scm> (define (add-one x) (+ x 1))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}