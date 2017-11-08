from datetime import datetime


class Interval():
    """
    May describe any measurable interval of time supported by the dataset.
    Contains a list of smaller intervals as a property.
    Can be used to process or list messages recursively.
    """
    pass


class Message():
    text: str
    author: str
    author_mode: str
    channel: str
    timestamp: datetime

    def __init__(self, text, author, year, month, day, hour, minute, second, channel, author_mode=None):
        Message.timestamp = datetime(year, month, day, hour, minute, second)
        Message.text = text
        Message.author = author
        Message.channel = channel
        Message.author_mode = author_mode if author_mode is not None else ''

    def __repr__(self):
        return f'In #{self.channel} on [{self.timestamp.year}/{self.timestamp.month}/{self.timestamp.day}] ' \
               f'at [{self.timestamp.hour:02d}:{self.timestamp.minute:02d}:{self.timestamp.second:02d}]' \
               f' <{self.author_mode}{self.author}> {self.text}'
