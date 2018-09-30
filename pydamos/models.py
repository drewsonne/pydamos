import json


class Clienter(object):
    def __init__(self, client: 'Client' = None):
        self._c = client

    _c = None


class IdValue(Clienter):
    def __repr__(self):
        return json.dumps({"id": self.id, "value": self.value})


class ItemIterator(Clienter):
    current = 1
    collection_id = 0

    def __init__(self, collection_id, client):
        super(ItemIterator, self).__init__(client)
        self.collection_id = collection_id

    def __iter__(self):
        return self

    def __next__(self):
        item = self._c.post('getitem', {
            # 'collection_id': self.collection_id,
            # 'item_id': self.current,
            'chosen_item_id': self.current,
        }, cls=Item)

        self.current = int(item.item_next)

        return item


class Collection(IdValue):
    id = int
    value = str

    def items(self):
        return ItemIterator(
            self.id,
            self._c
        )


class Writer(IdValue):
    id = int
    value = str


class Fragment(IdValue):
    id = int
    value = str


class Stylus(str, Clienter): pass


class Series(str, Clienter): pass


class Subseries(str, Clienter): pass


class Set(str, Clienter): pass


class GeoInfo(Clienter):
    name = str
    icon = str
    doticon = str
    geopoint = [float]

    def location(self):
        return Point(*self.geopoint)

    def __repr__(self):
        return json.dumps({
            'name': self.name,
            'icon': self.icon,
            'doticon': self.doticon,
            'geopoint': str(self.location())
        })


class Point(object):
    def __init__(self, *args):
        self.latitude = args[0]
        self.longitude = args[1]

    def __repr__(self):
        return json.dumps([self.latitude, self.longitude])


class Item(Clienter):
    item_next = int
    item_previous = int
    item_content = str
    item_name = str
    item_metadata = dict
    item_info = dict
    bibliography = str


class DamosRoot(Clienter):
    collection = [Collection]
    writer = [Writer]
    stylus = [Stylus]
    series = [Series]
    subseries = [Subseries]
    set = [Set]
    fragment = [Fragment]
    treff = int
    geoinfo = {str: GeoInfo}

    def items(self):
        return (
            ('collections', self.collection),
            ('writers', self.writer),
            ('styluses', self.stylus),
            ('series', self.series),
            ('subseries', self.subseries),
            ('set', self.set),
            ('fragments', self.fragment),
            ('treff', self.treff),
            ('geoinfo', self.geoinfo)
        )

    def __iter__(self):
        return iter(self.items())
