test = {
  'name': 'cube',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cube 2)
          2bfcd627609c82ebd017c2edfad00c89
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cube 3)
          748461e5d70d2d34436c8d3c5a04855e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cube 1)
          7cd20da6435c318b417f99ab831ac85e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}