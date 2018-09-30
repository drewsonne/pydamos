from pydamos.client import _client


def facets():
    return _client.facets()

def sites():
    return _client.sites()