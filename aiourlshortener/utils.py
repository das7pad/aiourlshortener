__all__ = (
    'url_validator',
    'validate_url',
)

import re


def url_validator(url: str) -> bool:
    """
    validate given string for valid url

    :param str url: string url

    :return: true if string is valid else false
    :rtype: bool
    """
    if url and isinstance(url, str) and re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', url):
        return True
    return False


def validate_url(func):
    def wrapper(self, url):
        if url_validator(url):
            return func(self, url)

        raise ValueError('invalid url: {}'.format(url))

    wrapper.__name__ = func.__name__
    return wrapper
