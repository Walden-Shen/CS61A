test = {
  'name': 'likeliest_child',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select word, category, dependency_type, dependent_category, ROUND(max_frequency, 5) from likeliest_child limit 20;
          ,|F|CONJ|NC|0.58108
          ZD|Z|COMP|S|0.75
          a|S|COMP|NC|0.78444
          a_partir_de|S|COMP|NC|0.84
          a_través_de|S|COMP|NC|0.75
          abdomen|NC|SPEC|DA|0.64286
          absceso|NC|MOD|A|0.58824
          acceder|VMN|OBLC|S|0.75
          actualidad|NC|SPEC|DA|0.73333
          actualización|NC|COMP|S|0.58333
          al|CS|COMP|VMN|0.95
          alguno|PI|COMP|S|0.85714
          ante|S|COMP|NC|0.65385
          antebrazo|NC|SPEC|DA|0.7619
          antes_de|S|COMP|NC|0.56
          aorta|NC|MOD|A|0.53333
          aplicable|A|COMP|S|0.83333
          aplicar|VMN|DO|NC|0.52632
          aprendiz|NC|MOD|S|0.72727
          arteria|NC|MOD|A|0.55357
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read lab13_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}