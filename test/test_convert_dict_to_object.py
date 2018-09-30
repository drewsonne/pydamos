from argparse import Namespace
from unittest import TestCase

from pydamos.dict_structs import convert_dict_to_object


class TestConvert_dict_to_object(TestCase):
    def test_convert_dict_to_object(self):
        class MockCollection(Namespace):
            id = int
            value = str

        class MockRoot(Namespace):
            collection = [MockCollection]

        response = convert_dict_to_object(
            MockRoot,
            {
                'collection': [
                    {
                        'id': 10,
                        'value': 'Foo'
                    }, {
                        'id': 20,
                        'value': 'Bar'
                    }
                ]
            }
        )

        expected = MockRoot(
            collection=[
                MockCollection(id=10, value='Foo'),
                MockCollection(id=20, value='Bar'),
            ]
        )

        self.assertEqual(expected, response)
