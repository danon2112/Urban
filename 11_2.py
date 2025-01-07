import inspect
from pprint import pprint

def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = [key for key in obj.__dict__.keys()]
    info['methods'] = dir(obj)
    info['module'] = obj.__module__
    return info

class Progger:
    def __init__(self, name):
        self.name = name
        self.grad = 'Junior'

    def get_info(self):
        return f'Name = {self.name}, grad = {self.grad}'

pg = Progger('Daniil')
# pprint(dir(pg))
pprint(introspection_info(pg))
