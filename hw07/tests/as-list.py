test = {
  'name': 'as-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (as-list (right odd-tree))
          6be41fb4a0d0c6c588d614ead76413ad
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list odd-tree)
          6d4f139fc7bb48dd186eefd7d3f1b46d
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