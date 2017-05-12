test = {
  'name': 'word_cat_count',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT word, category, count FROM word_cat_count WHERE word = "ser";
          ser|NC|15
          ser|VSG|8
          ser|VSI|2978
          ser|VSN|178
          ser|VSP|71
          ser|VSS|78
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}