test = {
  'name': 'open',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from open_locations where n >= 5;
          5
          7
          9
          10
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read quiz04.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}