import parser

def test_parser(line):
    parsed = parser.parse_message(line)
    assert parsed is not None, f'"{line}" was not parsed properly'
    for attr in ['text', 'name', 'modechar', 'month', 'day', 'hour', 'minute', 'second']:
        assert parsed.group(attr) is not None, f'{attr} was not properly parsed (is None)'


if __name__ == '__main__':
    test_parser('Nov 03 13:38:53 <+kageru>   :same:')
