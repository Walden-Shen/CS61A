test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sign -42)
          e1b9cfca7d7c90645adadc2693015138
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          2987fbac6d35b0de527489a12a63cba6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          c246989ba42191bcf781a5b9bc9b80ea
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}