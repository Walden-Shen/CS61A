test = {
  'name': 'filter',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(1 2 3 4))
          eefe2d916ae4b9218d146bc0277a63fa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(1 3 5))
          7d62d6f97eff3c26faed6c90e572e14b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(2 4 6))
          9fe2321549ca80f78f8bead3784a61a6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? nil)
          9fe2321549ca80f78f8bead3784a61a6
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