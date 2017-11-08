import re

pattern = re.compile(r'(?P<month>[^\s]+)\s(?P<day>\d{1,2})\s(?P<hour>\d{1,2}):(?P<minute>\d{1,2}):(?P<second>\d{1,2})\s<(?P<modechar>[^\w])?(?P<name>.*)>\s+(?P<text>.+)')


def parse_message(line, year=None):
    """
    Parses a single message from an IRC log.
    Year is not specified in the logs, so it must be passed explicitly.
    """
    return re.search(pattern, line)