from functools import lru_cache
from typing import List

from requests import Request, Session

from pydamos.dict_structs import convert_dict_to_object
from pydamos.models import Collection, DamosRoot, Writer, Stylus, Series, Subseries, Set, Fragment


class Client(object):
    ROOT_URL = 'https://www2.hf.uio.no/damos/index'

    def __init__(self):
        self._session = Session()

    def _do_call(self, method, path, cls=None, data=None):
        request = Request(
            method,
            self._build_url(path)
        )
        if data is not None:
            request.data = data
        response = self._session.send(
            request.prepare()
        )

        if response.status_code != 200:
            raise Exception("Bad status: " + str(response.status_code))

        if cls is None:
            return response.json()
        else:
            return convert_dict_to_object(cls, response.json(), self)

    def _build_url(self, path):
        return "{root}/{path}".format(
            root=self.ROOT_URL,
            path=path
        )

    @lru_cache(maxsize=256)
    def get(self, path, cls=None):
        return self._do_call('GET', path=path, cls=cls)

    def post(self, path, data, cls=None):
        return self._do_call('POST', path, cls=cls, data=data)

    def facets(self):
        return _client.get(path='ajaxmenu', cls=DamosRoot)

    def sites(self) -> List[Collection]:
        return self.facets().collection

    def writers(self) -> List[Writer]:
        return self.facets().writer

    def styluses(self) -> List[Stylus]:
        return self.facets().stylus

    def series(self) -> List[Series]:
        return self.facets().series

    def subseries(self) -> List[Subseries]:
        return self.facets().subseries

    def sets(self) -> List[Set]:
        return self.facets().set

    def fragments(self) -> List[Fragment]:
        return self.facets().fragment

    def treff(self) -> int:
        return self.facets().treff


_client = Client()
