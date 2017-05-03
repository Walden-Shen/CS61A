test = {
  'name': 'nodotss',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          3302d9cfb5424730d38e1800c58cb524
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          1e3073d18286464afe726301e6d6af5d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          0a16de72d68c8a83548ad334681bdb72
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          6184ea0bd692cb5555d31c4d0918c6b0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          6184ea0bd692cb5555d31c4d0918c6b0
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}