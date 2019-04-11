from flask import Blueprint


class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', f.__name__)
            self.mound.append((rule, f'{self.name}+{endpoint}', f, options))
            return f

        return decorator

    def register(self, bp: Blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for rule, endpoint, f, options in self.mound:
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
