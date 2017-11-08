from datetime import datetime


class Interval():
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
        return f'In #{self.channel} on [{self.timestamp.year}/{self.timestamp.month}/{self.timestamp.day}] ' + \
               'at [{:02d}:{:02d}:{:02d}]'.format(self.timestamp.hour, self.timestamp.minute, self.timestamp.second) + \
               f' <{self.author_mode}{self.author}> {self.text}'
