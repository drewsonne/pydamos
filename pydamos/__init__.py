from pydamos.client import _client
from pathlib import Path
import pyfscache




def set_cache_location(new_location):
    _config.set_cache_location(new_location)


def facets():
    return _client.facets()


def sites():
    return _client.sites()
