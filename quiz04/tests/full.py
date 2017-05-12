test = {
  'name': 'full',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select n, items from full where n >= 5;
          5|bagels, coffee, espresso
          7|espresso
          9|eggs, espresso
          10|eggs, espresso
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