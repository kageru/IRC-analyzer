from datetime import datetime


class Interval():
    pass


class Message():
    text: str
    author: str
    timestamp: datetime

    def __init__(self, text, author, year, month, day, hour, minute, second):
        Message.timestamp = datetime(year, month, day, hour, minute, second)
        Message.text = text
        Message.author = author
