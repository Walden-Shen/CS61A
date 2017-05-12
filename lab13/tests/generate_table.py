test = {
  'name': 'generate_table',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select count(*) from deps;
          124445
          sqlite> select count(distinct word) from deps;
          6872
          sqlite> select count(distinct category) from deps;
          37
          sqlite> select count(distinct dependent_category) from deps;
          38
          sqlite> select count(distinct dependent_word) from deps;
          7580
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .open spanish.db
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}