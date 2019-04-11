from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        super().default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder