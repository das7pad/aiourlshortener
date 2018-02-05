import inspect
from importlib.machinery import SourceFileLoader
import os

from .base import BaseShortener
from ..exceptions import UnknownAioUrlShortenerError

_shorten_class = {}
_path = os.path.dirname(os.path.realpath(__file__))
for file in os.listdir(_path):
    if file.startswith('__') or file == 'base.py':
        continue
    _shorten = SourceFileLoader('aiourlshortener.shorteners.', '{}/{}'.format(_path, file)).load_module()
    for attr in dir(_shorten):
        tmp_cls = getattr(_shorten, attr)
        if attr != 'BaseShortener' and inspect.isclass(tmp_cls) and issubclass(tmp_cls, BaseShortener) and not inspect.isabstract(tmp_cls):
            _shorten_class[attr] = tmp_cls

__all__ = ['Shorteners', 'Shortener']


class Shorteners(object):
    GOOGLE = 'Google'
    BITLY = 'Bitly'


def Shortener(engine, **kwargs):
    """Factory for all Shorteners"""
    if inspect.isclass(engine) and issubclass(engine, BaseShortener) and not inspect.isabstract(engine):
        return engine(**kwargs)
    elif engine in _shorten_class:
        return _shorten_class[engine](**kwargs)
    else:
        raise UnknownAioUrlShortenerError('Please enter a valid shortener. {} class does not exist'.
                                          format(engine))
