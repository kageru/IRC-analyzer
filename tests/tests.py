import irc_types
import parser

def test_parser(line):
    parsed = parser.parse(line)
    for attr in ['text', 'author', 'channel', 'timestamp']
        assert parsed.group(attr) is not None, f'{attr} was not properly parsed (is None)'