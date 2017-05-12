test = {
  'name': 'noun_verbs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from noun_verbs limit 10;
          deber|NC|17|deber|VMG|2
          deber|NC|17|deber|VMI|407
          deber|NC|17|deber|VMN|1
          deber|NC|17|deber|VMP|18
          deber|NC|17|deber|VMS|4
          despertar|NC|3|despertar|VMN|2
          haber|NC|2|haber|VAI|2
          haber|NC|2|haber|VMI|149
          haber|NC|2|haber|VMS|2
          poder|NC|26|poder|VMG|2
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