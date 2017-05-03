test = {
  'name': 'all-satisfies',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (all-satisfies '(1 2 3 4) even?)
          a4015fdedc66a98a3d74622fb751ee0a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (all-satisfies '(1 3 5) odd?)
          b2fd0f50cc6b6d79b0b844be1c0e8231
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (all-satisfies '(2 4 6) odd?)
          a4015fdedc66a98a3d74622fb751ee0a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (all-satisfies nil odd?)
          b2fd0f50cc6b6d79b0b844be1c0e8231
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09-extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}