test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2))
          77dd026e0de117cd093a3a2a76a09075
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3 . 4))
          49350b0cf533772189ff50e5dac3c962
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 (3 . 5)))
          49350b0cf533772189ff50e5dac3c962
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (how-many-dots '(6 . (6 . (6))))
          77dd026e0de117cd093a3a2a76a09075
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) . 3))
          97f7ea0bb9bb6ef002baa72d4b074a37
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) (3 . 4) 5 . 6))
          ec3614910efb1e7bff4995d672254fe7
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}