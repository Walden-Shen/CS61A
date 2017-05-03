test = {
  'name': 'in?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (in? odd-tree 1)
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? odd-tree 2)
          30fee613b5f24feb0ea2d5089730e609
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? odd-tree 3)
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? odd-tree 4)
          30fee613b5f24feb0ea2d5089730e609
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? odd-tree 5)
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      scm> (define odd-tree (tree 3 (leaf 1)
      ....                          (tree 7 (leaf 5)
      ....                                  (tree 9 nil (leaf 11)))))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}